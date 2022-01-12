import os

import __root__


def report():
    pass
    # os.mkdir("Reports/LatestResults")
    reports = os.path.join(__root__.path(), "Reports")
    screenshots = os.path.join(__root__.path(), "Reports/Screenshots")
    log_path = os.path.join(__root__.path(), "Reports/Logs.log")
    report_path = os.path.join(__root__.path(), "Reports/Report.html")

    if not os.path.exists(reports):
        os.mkdir(reports)
        os.mkdir(screenshots)
    # if not os.path.exists(latest_results):
    #     os.mkdir(latest_results)
    if not os.path.exists(screenshots):
        os.mkdir(screenshots)
    if os.path.exists(log_path):
        os.remove(log_path)
    if os.path.exists(report_path):
        os.remove(report_path)


if __name__ == '__main__':
    report()

