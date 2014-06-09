import System
static def GetAttributeValue(Incident):
    
	# unknown why set Boolean like so...?
	VarTrue = true
    VarFalse = false
	
	# all the windows
	hardware_purchase = 	":SetHidden(_HardwarePurchase1,{0};:SetMandatory(_HardwarePurchase1,{1};"
	configuration_item = 	":SetHidden(ConfigurationItem,{2});:SetMandatory(ConfigurationItem,{3});"
	account_type = 			":SetHidden(_AccountType,{4});:SetMandatory(_AccountType,{5});"
	device_type = 			":SetHidden(_DeviceType1,{6});:SetMandatory(_DeviceType1,{7});"
	room = 					":SetHidden(_Room,{8});:SetMandatory(_Room,{9});"
	ein = 					":SetHidden(_EIN,{10});:SetMandatory(_EIN,{11});"
	grades_requested = 		":SetHidden(_GradesRequested,{12});:SetMandatory(_GradesRequested,{13});"
	classes_requested = 	":SetHidden(_ClassesRequested,{14});:SetMandatory(_ClassesRequested,{15});"
	home_or_work = 			":SetHidden(_HomeorWork1,{16});:SetMandatory(_HomeorWork1,{17});"
	operating_system = 		":SetHidden(_OperatingSystem1,{18});:SetMandatory(_OperatingSystem1,{19});"
	browser = 				":SetHidden(_Browser1,{20});:SetMandatory(_Browser1,{21});"
	peripheral_type = 		":SetHidden(_PeripheralType1,{22});:SetMandatory(_PeripheralType1,{23});"
	timeframe = 			":SetHidden(_Timeframe,{24});:SetMandatory(_Timeframe,{25});"
	attendance_scanners = 	":SetHidden(_AttendanceScanners1,{26});:SetMandatory(_AttendanceScanners1,{27});"
	url = 					":SetHidden(_URL,{28});:SetMandatory(_URL,{29});"
	smartphone_type = 		":SetHidden(_SmartphoneType1,{30});:SetMandatory(_SmartphoneType1,{31});"
	budget_code = 			":SetHidden(_BudgetCode,{32});:SetMandatory(_BudgetCode,{33});"
	software_purchase = 	":SetHidden(_SoftwarePurchase1,{34});:SetMandatory(_SoftwarePurchase1,{35});"
	asset_id = 				":SetHidden(_AssetID,{36});:SetMandatory(_AssetID,{37});"
	library_request = 		":SetHidden(_LibraryRequest1,{38});:SetMandatory(_LibraryRequest1,{39});"	

	all_windows = hardware_purchase + configuration_item + account_type + device_type + room + ein + grades_requested + home_or_work + operating_system + browser + peripheral_type + timeframe + attendance_scanners + url + smartphone_type + budget_code  + software_purchase + asset_id + library_request
	
        if Incident.Category != null and Incident.Category.FullName.Contains("Access.Password.NONPAL"):
            return String.Format(all_windows, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
 		elif Incident.Category != null and Incident.Category.FullName.Contains("Access.Password.Telephone"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
 		elif Incident.Category != null and Incident.Category.FullName.Contains("Access.Password.CollectionPlus"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Access.NewAccount.ALL"):
            return String.Format(all_windows, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Access.Network"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Access.Other"):
            return String.Format(all_windows, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Hardware.Computer"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Hardware.Printer"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Hardware.Network"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Hardware.Peripherals"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Hardware.AttendanceScanners"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Hardware.PortableDevice"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Software.AdminApps"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Software.Trillium"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Software.TWEA"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Software.CollectionPlus"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Software.WordPress"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Software.Other"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Communication.Telephone"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Communication.Smartphone"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Communication.HearingDevice"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Broken.Other"):
            return String.Format(all_windows, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Question.Software.AdminApps"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Question.Software.StudentSystem"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Question.Software.TWEA"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Question.Software.CollectionPlus"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Question.Software.WordPress"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Hardware.Purchase"):
            return String.Format(all_windows, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Software.Purchase"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Software.Install"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Library.Request"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Network.Request"):
            return String.Format(all_windows, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Report.DataWarehouse"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category != null and Incident.Category.FullName.Contains("Order.Hardware.NewEmployeeRequest"):
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        elif Incident.Category == null:
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        else:
            return String.Format(all_windows, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)