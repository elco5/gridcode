import powerwall, voltwatt, reportdriver

report = reportdriver.ReportDriver()    # new report
pw = powerwall.Powerwall()          # create eut
vw1 = voltwatt.VoltWattTest(1, pw)  # create test data profile

ideal = report.calc_ideal_power_data_frame(vw1)
