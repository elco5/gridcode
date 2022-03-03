
import powerwall, voltwatt, reportdriver, bento

report = reportdriver.ReportDriver()    # new report
pw = powerwall.Powerwall()          # create eut
bto = bento.Bento()
vw1 = voltwatt.VoltWattTest(1, pw)  # create test data profile

ideal = report.calc_ideal_power_data_frame(vw1)
test_steps = report.calc_test_steps_power_data_frame(vw1)
