# URL: http://tungwaiyip.info/software/HTMLTestRunner.html

__author__ = "Wai Yip Tung"
__version__ = "0.8.2"

import datetime as datetime
from io import StringIO
import sys
import os
import unittest
import csv
from xml.sax import saxutils
from subprocess import Popen, PIPE


class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


class Template_mixin(object):
    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
        3: 'knownFail',
        4: 'blacklistPass',
    }

    DEFAULT_TITLE = 'Integration Test Report'
    DEFAULT_DESCRIPTION = ''

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""
    <!DOCTYPE html>
    <html lang="de">
        <head>
            <meta charset="utf-8">
            <title>%(title)s</title>
            <meta name="generator" content="%(generator)s"/>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
            %(stylesheet)s
        </head>
        <body>
            <script language="javascript" type="text/javascript"><!--
            output_list = Array();

            /* level - 0:Summary; 1:Failed; 2:All */
            function showCase(level) {
                trs = document.getElementsByTagName("tr");
                for (var i = 0; i < trs.length; i++) {
                    tr = trs[i];
                    id = tr.id;
                    if (id.substr(0,2) == 'ft') {
                        if (level < 1) {
                            tr.className = 'hiddenRow';
                        }
                        else {
                            tr.className = '';
                        }
                    }
                    if (id.substr(0,2) == 'pt') {
                        if (level > 1) {
                            tr.className = '';
                        }
                        else {
                            tr.className = 'hiddenRow';
                        }
                    }
                }
            }


            function showClassDetail(cid, count) {
                var id_list = Array(count);
                var toHide = 1;
                for (var i = 0; i < count; i++) {
                    tid0 = 't' + cid.substr(1) + '.' + (i+1);
                    tid = 'f' + tid0;
                    tr = document.getElementById(tid);
                    if (!tr) {
                        tid = 'p' + tid0;
                        tr = document.getElementById(tid);
                    }
                    id_list[i] = tid;
                    if (tr.className) {
                        toHide = 0;
                    }
                }
                for (var i = 0; i < count; i++) {
                    tid = id_list[i];
                    if (toHide) {
                        document.getElementById('div_'+tid).style.display = 'none'
                        document.getElementById(tid).className = 'hiddenRow';
                    }
                    else {
                        document.getElementById(tid).className = '';
                    }
                }
            }


            function showTestDetail(div_id){
                var details_div = document.getElementById(div_id)
                var displayState = details_div.style.display
                if (displayState != 'block' ) {
                    displayState = 'block'
                    details_div.style.display = 'block'
                }
                else {
                    details_div.style.display = 'none'
                }
            }

                function html_escape(s) {
                s = s.replace(/&/g,'&amp;');
                s = s.replace(/</g,'&lt;');
                s = s.replace(/>/g,'&gt;');
                return s;
            }

            --></script>

        %(heading)s
        %(report)s
        %(ending)s

        </body>
    </html>
    """

    STYLESHEET_TMPL = """
    <style type="text/css" media="screen">
    body        
    { 
        font-family: verdana, arial, helvetica, sans-serif; 
        font-size: 12px;
        background-color: #F8F8FF;
    }
    div.heading
    {
        position:absolute;
        left: 0px;
        top: 0px;
        width: 100%;
        min-width: 1650px;
    }
    .attribute 
    {
        margin-top: 1ex;
        margin-bottom: 0;
    }
    .subject
    {
        font-size: 16px;
        font-weight: bold;
        color: #555;
        background-color: #FF9833;
        padding: 10px 50px 15px;
        box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.1);
    }
    .testData
    {
        position: relative;
        display: block;
        height: 180px;
        width: 20%;
        min-width: 400px;
        border: 1px solid #EEE;
        margin: 10px;
        background-color: #FFF;
        box-shadow: 1px 1px 5px 1px rgba(0,0,0,0.17);
        float: left;
        padding: 0 10px;
        overflow:auto;
        overflow-x: hidden;
    }
    .testDataSubject
    {
        width: 100%;
        padding-left: 20%;
        color: #555;
        font-size: 15px;
        font-style: italic;
    }
    .passPercentage
    {
        text-align: center;
        margin-top: 50px;
        font-size: 30px;				
    }

    div.main
    {
        position:relative;
        left: 0px;
        top: 260px;
        width: 99%;
        min-width:1650px;
        border: 1px solid #EEE;
        background-color: #FFF;
        box-shadow: 1px 1px 5px 1px rgba(0,0,0,0.17);
    }
    #result_table { width: 100%; }
    th, td
    {
        padding: 5px;
        text-align: center;
    }
    td
    {
        border-top: 1px solid #DDD;
    }
    .resultButton
    {
        border-radius: 3px;
        padding: 2px 15px;
        cursor: pointer;
        color: #333;
        text-decoration: none;
        background-color: #F8F8FF;
        transition: background-color 0.8s ease;
    }
    .resultButton:hover { background-color: #C0C0C0; }

    a.popup_link 
    {
        text-decoration: none;
        text-transform: uppercase;
        color: #000000;
        background-color: #DDDDDD;
        border-radius: 3px;
        padding: 2px 20px;
        transition: background-color 0.8s ease;
    }

    a.popup_link:hover 
    {
        color: #555555;
        background-color: #EEEEEE;
    }

    .popup_window 
    {
        display: none;
        position: relative;
        left: 0px;
        top: 0px;
        padding: 2%;
        background-color: #ECECEC;
        text-align: left;
        text-justify: inter-word;
        font-size: 8pt;
        width: 96%;
        word-wrap: break-word;
        margin: 10px 0px;
        min-with:800px;
    }
     #show_detail_line { margin-left: 5px; }
    .passClass  { background-color: #6c6; }
    .failClass  { background-color: #c60; }
    .knownFailClass  { background-color: yellow; }
    .blacklistPassClass  { background-color: yellow; }
    .errorClass { background-color: #c00; }
    .passCase   { color: #6c6; }
    .failCase   { color: #c60; font-weight: bold; }
    .knownFailCase   { color: #c60; font-weight: bold; }
    .blacklistPassCase   { color: #c60; font-weight: bold; }
    .errorCase  { color: #c00; font-weight: bold; }
    .hiddenRow  { display: none; }
    .testcase   { margin-left: 2em; }
    a.fail      { background-color: #c60; }
    a.knownFail      { background-color: #FFD700; }
    a.blacklistPass      { background-color: #7ab87a; }
    a.pass      { background-color: #6c6; }
    a.error     { background-color: #c00; }
    #total_row  { background-color: #DDD; }
    a.showButton
    {
        padding: 3px 10px;
        margin: 0px 5px;
        text-decoration: none;
        background-color: #E8E8EE;
        color: #333;
        border-radius: 3px;
        transition: background-color 0.8s ease;
    }
    a.showButton:hover { background-color: #D8D8DD; }
    div.quickStatus
    {
        margin: 0px auto;
        width: 100px;
        height: 15px;
        background-color: #c00;
        border-radius: 2px;
        border: 1px solid #E8E8EE;
    }
    .tooltip 
    {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
    }

    .tooltip .tooltiptext 
    {
        visibility: hidden;
        width: 60px;
        background-color: #D8D8DD;
        color: #555;
        text-align: center;
        border-radius: 3px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -30px;
        opacity: 0;
        transition: opacity 0.6s;
        transition-delay: 0.3s;
        }

    .tooltip .tooltiptext::after 
    {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #D8D8DD transparent transparent transparent;
    }

    .tooltip:hover .tooltiptext
    {
        visibility: visible;
        opacity: 1;
    }
    </style>
    """

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """
    <div class="heading">
        <div class="subject">%(title)s</div>
        <div class="testData">
            <p class="testDataSubject">Test Data</p>
            %(parameters)s
            <p class='description'>%(description)s</p>
        </div>
        <div class="testData">
            <p class="testDataSubject">Selected test summary</p>
            %(summary)s
        </div>
        <div class="testData">
            <p class="testDataSubject">Pass percentage</p>
            <p class="passPercentage">%(passPercentage)s %%</p>
        </div>
    </div>    
    """  # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s:</strong> %(value)s</p>
"""  # variables: (name, value)

    HEADING_SUMMARY_TMPL = """
    <p class='attribute'>
        <div style='width: 100px; float:left;'>
            <strong>%(name)s:</strong>
        </div>
        <div>  
            %(value)s
        </div>
    </p>
    """

    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """
    <div class="main">
        <p id='show_detail_line'>Shortcuts: 
            <a href='javascript:showCase(0)' class='showButton'>Summary</a>
            <a href='javascript:showCase(1)' class='showButton'>Failed</a>
            <a href='javascript:showCase(2)' class='showButton'>All</a>
        </p>
        <table id='result_table'>
            <colgroup>
                <col align='left' />
                <col align='center' />
                <col align='center' />
                <col align='center' />
                <col align='center' />
                <col align='center' />
                <col align='center' />
            </colgroup>
            <tr>
                <th width='50%%'>Test group/Test case</th>
                <th width='7%%'>Count</th>
                <th width='7%%'>Pass</th>
                <th width='7%%'>Fail</th>
                <th width='7%%'>Error</th>
                <th width='11%%'>Result</th>
                <th width='11%%'>QuickStatus</th>
            </tr>
            %(test_list)s
            <tr id='total_row'>
                <td>Total</td>
                <td>%(count)s</td>
                <td>%(Pass)s</td>
                <td>%(fail)s</td>
                <td>%(error)s</td>
                <td></td>
                <td></td>
            </tr>
        </table>
    </div>  
"""  # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
    <tr class='%(style)s'>
        <td>%(desc)s</td>
        <td>%(count)s</td>
        <td>%(Pass)s</td>
        <td>%(fail)s</td>
        <td>%(error)s</td>
        <td>
            <a href="javascript:showClassDetail('%(cid)s',%(count)s)" class="resultButton">
                Detail
            </a>
        </td>
        <td>
            <div class='quickStatus tooltip'><span class="tooltiptext">%(quickState)s %%</span>
                <div style='background-color: green; height: 15px; width: %(quickState)spx'></div>
            </div>
        </td>
    </tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='6' align='center'>

    <!--css div popup start-->
    <a class="popup_link %(status)s" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s
    </a>

    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color: black; cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        %(script)s
        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='6' align='center'>%(status)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #

    ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.outputBuffer = StringIO
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        self.lastFailedTestName = "n/a"
        self.lastFailedTestReason = "n/a"
        self.lastFailedTestDetectionDate = "n/a"
        self.lastFailedTestTask = "n/a"
        self.lastFailedTestVariant = "All"

        self.aHeadLine = None
        self.aTestData = None

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []

    def isTestInBlacklist(self, failedTestFullName):
        bIsTestBlacklisted = False
        aFailedTestName = failedTestFullName.__str__().split()
        sFailedTestName = aFailedTestName[0]

        workspacePath = __file__[0] + ":\\frdcc_i_e_mobility\\ecaravan\\testing\\test_framework"
        libraryPath = workspacePath + "\\Library"
        blackListPath = libraryPath + '\\RegressionBlackList.csv'
        iLine = 0
        with open(blackListPath) as csvFile:
            RegressionBlackListReader = csv.reader(csvFile, delimiter=";")
            for tests in RegressionBlackListReader:
                if iLine == 0:
                    self.aHeadLine = tests.__str__().split(",")
                if sFailedTestName in tests:
                    aFailedTest = tests.__str__().split(",")
                    self.aTestData = aFailedTest
                    self.lastFailedTestName = failedTestFullName
                    self.lastFailedTestReason = aFailedTest[2]
                    self.lastFailedTestDetectionDate = aFailedTest[3]
                    self.lastFailedTestVariant = aFailedTest[8]
                    bIsTestBlacklisted = True
                iLine += 1
            return bIsTestBlacklisted

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()

    def addSuccess(self, test):
        """
        if self.isTestInBlacklist(test):
            print("\nPASSED TEST IN BLACKLIST => Test [%s] \n is currently in blacklist but passing\n\n" % test)
            for iIndex in range(len(self.aHeadLine)):
                sKey = self.aHeadLine[iIndex].replace("'", "").replace("[", "").replace("]", "").upper()
                sValue = self.aTestData[iIndex].replace("'", "").replace("[", "").replace("]", "")
                print("%s: %s" % (sKey, sValue))
            print("\n")
        """

        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok \t')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E \t')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        """
        if self.isTestInBlacklist(test):
            print("\nKNOWN FAILED => Test [%s] \n is currently in blacklist\n\n" % test)
            for iIndex in range(len(self.aHeadLine)):
                sKey = self.aHeadLine[iIndex].replace("'", "").replace("[", "").replace("]", "").upper()
                sValue = self.aTestData[iIndex]. replace("'", "").replace("[", "").replace("]", "")
                print ("%s: %s" % (sKey, sValue))
            print("\n")
        else:
            print("\nUNKNOWN FAILED => This test fail is currently unknown and not in blacklist\n")
        self.failure_count += 1
        """
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F \t')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')


class HTMLTestRunner(Template_mixin):

    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None):
        self.stopTime = datetime.datetime.now()
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def isTestInBlacklist(self, failedTestFullName):
        aFailedTestName = failedTestFullName.__str__().split()
        sFailedTestName = aFailedTestName[0]

        pattWorkspace = __file__[0] + ":\\frdcc_i_e_mobility\\ecaravan\\testing\\test_framework"
        libraryPath = pattWorkspace + "\\Library"
        blackListPath = libraryPath + '\\RegressionBlackList.csv'
        with open(blackListPath) as csvFile:
            RegressionBlackListReader = csv.reader(csvFile, delimiter=";")
            for tests in RegressionBlackListReader:
                if sFailedTestName in tests:
                    return True

                    # aBlackListData = tests.__str__().split(",")
                    # print (aBlackListData)
                    # sVariantsFromBl = aBlackListData[8]
                    # if sVariantsFromBl == " '']":
                    #     print("\nKnown failed detected. Test [%s] is listed in Blacklist" % failedTestFullName)
                    #     return True
                    # aVariantsFromBL = sVariantsFromBl.split(" ")
                    # for variant in aVariantsFromBL:
                    #     variant = variant.replace("'", "").replace("]", "")
                    #     if variant != "" and variant in self.description:
                    #         print("\nKnown failed detected. Test [%s] is listed in Blacklist" % failedTestFullName)
                    #         return True
        return False

    def run(self, test):
        """Run the given test case or test suite."""
        result = _TestResult(self.verbosity)
        test(result)
        self.generateReport(test, result)
        # print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime)
        print(sys.stderr, '\nTime Elapsed=%s' % (self.stopTime - self.startTime))
        return result

    @staticmethod
    def sortResult(result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rMap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if cls not in rMap:
                rMap[cls] = []
                classes.append(cls)
            rMap[cls].append((n, t, o, e))
        r = [(cls, rMap[cls]) for cls in classes]
        return r

    @staticmethod
    def getSummary(result):
        iTotalTestCounter = result.success_count + result.failure_count + result.error_count
        return [('Total', iTotalTestCounter),
                ('Pass', result.success_count),
                ('Fail', result.failure_count),
                ('Error', result.error_count)]

    @staticmethod
    def getPassPercentage(result):
        iTotalTestCounter = result.success_count + result.failure_count + result.error_count
        if iTotalTestCounter == 0:
            return 0
        passPercentage = (result.success_count * 100) / iTotalTestCounter
        return passPercentage

    def getReportAttributes(self, result):
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        return [
            ('Start Time', startTime),
            ('Duration', duration),
            ('Plattform', self.getPlatform()),
            ('Working view', self.getCurrentView()),
            ('Variant', self.description),
        ]

    @staticmethod
    def getCurrentView():
        command = "cleartool pwv -short"
        pipe = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        while True:
            cmdLine = pipe.stdout.readline()
            if cmdLine:
                return cmdLine
            if not cmdLine:
                break

    @staticmethod
    def getPlatform():
        try:
            return os.environ["PROJECT_PLATTFORM"]
        except:
            return "SIL"

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        summary_attrs = self.getSummary(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        passPercentage = self.getPassPercentage(result)
        heading = self._generate_heading(report_attrs, summary_attrs, passPercentage)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
        )
        reportFileName = f"Unittest_{self.stopTime}"
        reportFileName = reportFileName.replace(" ", "_")
        reportFileName = reportFileName.replace(":", "_")
        reportFileName = reportFileName.replace(".", "_")
        reportFileName = reportFileName + ".html"
        try:
            file = open("./Unittests/Reports/" + reportFileName, "w")
            file.write(output)
        except:
            print('*')
            pass

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs, summary_attrs, passPercentage):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                name=saxutils.escape(name),
                value=value,
                # value=saxutils.escape(value),
            )
            a_lines.append(line)
        summary_lines = []
        for name, value in summary_attrs:
            line = self.HEADING_SUMMARY_TMPL % dict(
                name=name,
                value=value,
            )
            summary_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            summary=''.join(summary_lines),
            passPercentage=passPercentage,
            description='',
        )
        return heading

    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name
            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                quickState=(np * 100) / (np + nf + ne),
                cid='c%s' % (cid + 1),
            )
            rows.append(row)
            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL
        """
        if n == 1:
            if self.isTestInBlacklist(name):
                n = 3
        elif n == 0:
            if self.isTestInBlacklist(name):
                n = 4
        """
        # o and e should be byte string because they are collected from stdout and stderr?
        # if isinstance(o, str):
        #     # uo = unicode(o.encode('string_escape'))
        #     # uo = o.decode('latin-1')
        #     uo = e
        # else:
        #     uo = o
        # if isinstance(e, str):
        #     # ue = unicode(e.encode('string_escape'))
        #     # ue = e.decode('latin-1')
        #     ue = e
        # else:
        #     ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(o + e),
            # output=saxutils.escape(uo + ue),
        )
        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (n == 3 and 'knownFailCase') or (n == 1 and 'failCase' or 'none') or (
                        n == 4 and 'blacklistPassCase'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
        )
        row = row.replace("[[&lt;", "<")
        row = row.replace("&gt;]]", ">")
        row = row.replace("AssertionError:", "<span style=\"color: #ff0000; font-weight: bold\">AssertionError:")
        row = row.replace("AttributeError:", "<span style=\"color: #ff0000; font-weight: bold\">AttributeError:")
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL

    @classmethod
    def HTMLTestRunner(cls, stream, title, description, verbosity):
        pass


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def __init__(self):
        self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        self.verbosity = 2

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            pass
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
