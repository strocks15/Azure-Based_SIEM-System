Developed SIEM a software solution designed to provide real-time analysis of intrusions (Nmap scans, Shell attacks) using Azure Cloud Platform software gathered and combined log data (RDP Logins &amp; Failed RDP Logins) produced across the organization's technological infrastructure. • Approximately, 72,250 attacks being captured.

1. Introduction
      - Purpose and importance of a Security Information and Event Management (SIEM) system
      - Project goals and objectives
2. Preview of Technical Steps
3. Creating Azure Subscription
4. Creating Virtual Machine
5. Set up Microsoft Defender for Cloud
6. Creating Log Analytics Workspace
7. Enabling Gathering VM Logs in Security Center
8. Connecting Log Analytics to VM
9. Setting up Azure Sentinel
10.Logging into VM with Remote Desktop (Failed Logon)
11.Observing Event Viewer Logs in VM
12.Create PowerShell Script
13.Obtaining Geolocation.io API Key
14.Running Script to Retrieve Geo Data of Attackers
15.Creating Custom Log in Log Analytics Workspace
16.Creating Custom Fields/Extracting Fields from Raw Custom Log Data
17.Testing Extracts
18.Setting up Map in Sentinel with Latitude and Longitude (or Country)
19.Fixing Map Plot Sizes
20.Attack Scenario: China Begins Attacking
21.Attack Scenario: Taiwan Joins the Attack
22.Attack Scenario: Philippines Joins the Attack
23.Attack Scenario: Russia + Rest of the World Join in on the Attack
24.Final Check on Map
25.Final Thoughts and Takeaways
26.Attack Report Red Team
27.Conclusion
28.References  Introduction

Purpose and importance of a Security Information and Event Management (SIEM) system The purpose of a Security Information and Event Management (SIEM) system, as indicated in the given content, is to enhance security monitoring and incident response capabilities. A SIEM system combines the functionalities of security information management (SIM) and security event management (SEM), providing a comprehensive solution for collecting, analyzing, and correlating security-related data.

The importance of a SIEM system lies in its ability to detect and respond to security incidents in real-time. By aggregating logs and event data from various sources, such as network devices, servers, applications, and endpoints, a SIEM system can identify patterns, anomalies, and potential security threats. This enables security teams to proactively monitor the environment, identify malicious activities, and initiate timely incident response actions.

In the context of the provided content, the SIEM implementation using Azure services allows for efficient log collection, analysis, and visualization. By leveraging Azure Sentinel as the SIEM solution, the project aims to centralize and correlate logs, providing a holistic view of the security posture. Additionally, the project incorporates geolocation tracking of attackers, which further enhances the ability to detect and attribute potential threats.

Overall, a SIEM system is essential for organizations to improve their security posture, detect and respond to security incidents promptly, comply with regulatory requirements, and gain valuable insights into their infrastructure's security landscape.

Project goals and objectives Based on the provided content, here is an overview of the project goals and objectives for your SIEM implementation:

Goal: Implement a comprehensive SIEM solution using Azure services to enhance security monitoring and incident response capabilities.

Objectives:

1. Setup Infrastructure:
   - Create an Azure subscription to leverage cloud resources.
   - Deploy a virtual machine (VM) as the host for the SIEM system.
   - Configure firewall settings to allow necessary network traffic.
2. Log Collection and Analysis:
   - Create a Log Analytics Workspace in Azure to collect and store logs.
   - Enable log gathering for the VM in Azure Security Center.
   - Connect the Log Analytics Workspace to the VM to facilitate log collection.
   - Set up Azure Sentinel as the SIEM solution for log analysis.
3. Investigate Security Events:
   - Access the VM through Remote Desktop and document failed logon attempts.
   - Review Event Viewer logs on the VM to identify potential security events.
4. Geolocation Tracking of Attackers:
   - Download a PowerShell script to retrieve geolocation data.
   - Obtain an API key from Geolocation.io for geolocation services.
   - Execute the PowerShell script to gather geolocation data for attackers.
   - Create a custom log in the Log Analytics Workspace to store the geolocation data.
5. Data Extraction and Visualization:
   - Extract relevant information from the raw custom log data.
   - Test and validate the extraction process for accuracy.
   - Configure a map visualization in Azure Sentinel using latitude and longitude or country data.
   - Adjust map plot sizes for better visualization.
6. Simulated Attack Scenarios:
   - Simulate attack scenarios where different countries initiate and join attacks.
   - Document the geolocation data of attackers from each simulated scenario.
7. Final Review and Takeaways:
   - Perform a final check on the map visualization and ensure accuracy of data.
   - Reflect on the findings and observations from the project.
   - Summarize the key takeaways and insights gained from the SIEM implementation.
*Preview of Technical Steps*
Setting up a comprehensive SIEM system requires several technical steps to be completed. The following steps provide an overview of the process:

1. Create Azure Subscription:
    - Create an Azure subscription to access Azure services and resources.
2. Deploy Virtual Machine:
     - Create a virtual machine (VM) in Azure to serve as the host for the SIEM deployment.
     - Configure the VM with appropriate specifications and settings.
3. Configure Firewall:
     - Allow necessary network traffic by configuring firewall settings for the VM.
     - Ensure that the SIEM solution can communicate with relevant data sources.
4. Create Log Analytics Workspace:
    - Set up a Log Analytics Workspace in Azure to collect and store logs.
    - Configure the workspace to gather log data from various sources.
5. Enable Log Gathering in Security Center:
    - Enable log gathering for the VM in Azure Security Center.
    - Ensure that security logs and events from the VM are collected for analysis.
6. Connect Log Analytics to VM:
    - Establish a connection between the Log Analytics Workspace and the VM.
    - Enable log forwarding from the VM to the Log Analytics Workspace.
7. Set up Azure Sentinel:
    - Configure Azure Sentinel, a cloud-native SIEM solution, for log analysis.
    - Enable necessary features and functionalities within Azure Sentinel.
8.  Perform Initial Logon to VM:
    - Log in to the VM using Remote Desktop or another appropriate method.
    - Ensure that the initial logon is successful and access to the VM is established.
9. Review Event Viewer Logs:
    - Access the Event Viewer on the VM and review the logs.
    - Look for any potential security events or anomalies that may require further investigation.
 10. Customize Log Collection:
    - Implement any necessary customizations to enhance log collection.
    - Fine-tune log collection settings based on specific requirements.
11. Implement Additional Security Measures:
    - Configure additional security measures such as intrusion detection systems (IDS), antivirus software, or firewalls.
    - Integrate these security solutions with the SIEM system for enhanced security monitoring.
12. Test and Validate:
    - Perform testing and validation of the SIEM system's functionality.
    - Ensure that logs are being collected, analyzed, and correlated effectively.

*Creating Azure Subscription To create an Azure Free Subscription, follow these steps:*

1. Visit the Azure website: Go to the Azure portal at https://portal.azure.com/.
2. Sign in or create a new account: If you already have an Azure account, sign in using your credentials. Otherwise, click on the "Start free" button to create a new account.
3. Create a new Azure subscription: Once signed in, click on the "Create a resource" button located on the left side of the Azure portal.
4. Select the "Subscription" option: In the search bar, type "Subscription" and select the "Subscription" option from the search results.
5. Click on the "Add" button: On the Subscription page, click on the "Add" button to create a new subscription.
6. Fill in the subscription details: Provide the required information, such as the subscription name, directory, offer type, and other relevant details.
7. Choose the Free subscription offer: Under the "Offers" section, select the "Free subscription" option.
8. Review and agree to the terms: Read through the terms and conditions, and once you agree, check the box to accept them.
9. Click on the "Create" button: After reviewing and accepting the terms, click on the "Create" button to create your Azure Free Subscription.
10. Wait for the subscription to be created: Azure will now create your Free Subscription. This process may take a few moments.
11. Access your Free Subscription: Once the subscription is created, you will receive a confirmation. You can now access and manage your Free Subscription through the Azure portal.

*Creating Virtual Machine8

To create a virtual machine (VM) in Azure, follow these steps:
1. Sign in to the Azure portal: Go to https://portal.azure.com and sign in using your Azure account credentials.
2. Navigate to the "Virtual Machines" page: Once signed in, click on the "Virtual Machines" option in the left-hand menu or use the search bar to locate and select "Virtual Machines" from the search results.
3. Click on the "Add" button: On the Virtual Machines page, click on the "+ Add" button to start creating a new VM.
4. Select a base image: In the "Basics" tab, select the desired operating system image for your VM. You can choose from various pre-configured images provided by Azure or use your own custom image.
5. Specify VM details: Provide the following information:
    - Subscription: Select your Azure subscription.
    - Resource group: Choose an existing resource group or create a new one.
    - Virtual machine name: Enter a unique name for your VM.
    - Region: Select the Azure region where you want to deploy the VM.
    - Availability options: Choose the availability options that suit your requirements.
    - Size: Select the VM size based on the required compute and memory resources.
    - Authentication type: Choose either password-based or SSH key-based authentication.
6. Configure additional settings: You can customize settings such as storage, networking, management, and monitoring as per your requirements. These settings include disk type, virtual network, subnet, public IP address, and more.
7. Review and create: Review all the configurations you have made so far, and then click on the "Review + Create" button.
8. Validate and deploy: Azure will validate your configuration settings. If there are no errors, click on the "Create" button to start the deployment process.
9. Monitor deployment: Azure will begin deploying your VM based on the specified settings. You can monitor the deployment progress on the Azure portal.
10. Access and manage your VM: Once the deployment is complete, you can access and manage your VM through the Azure portal. You may need to note down the public IP address or DNS name assigned to your VM for remote access.

*Set up Microsoft Defender for Cloud To set up Microsoft Defender for Cloud in an Azure environment, you can follow these steps:*

1. Sign in to the Azure portal: Go to https://portal.azure.com and sign in using your Azure account credentials.
2. Create a Microsoft Defender for Cloud workspace: In the Azure portal, search for "Microsoft Defender for Cloud" in the search bar. Select the service from the results and click on "Create" to start the workspace creation process.
3. Configure the workspace settings:
    - Subscription: Choose the Azure subscription where you want to create the workspace.
    - Resource group: Select an existing resource group or create a new one.
    - Workspace name: Provide a name for the Microsoft Defender for Cloud workspace.
    - Region: Choose the Azure region where you want to deploy the workspace.
    - Pricing tier: Select the appropriate pricing tier based on your requirements and budget.
4. Configure data sources: In the "Data sources" section, select the Azure resources that you want to monitor and protect using Microsoft Defender for Cloud. You can choose from options such as Azure Active Directory, Azure Kubernetes Service (AKS), Azure Container Registry (ACR), and more.
5. Enable security controls: In the "Security controls" section, you can enable specific security controls provided by Microsoft Defender for Cloud. These controls include vulnerability assessment, adaptive application control, just-in-time (JIT) VM access, and more. Choose the controls that align with your security requirements.
6. Configure threat intelligence settings: In the "Threat intelligence" section, you can enable threat intelligence feeds to enhance the detection and response capabilities of Microsoft Defender for Cloud. You can choose from Microsoft's threat intelligence feeds and also add custom indicators of compromise (IoCs) if needed.
7. Review and create the workspace: Review the configuration settings you have chosen for the Microsoft Defender for Cloud workspace. If everything looks correct, click on "Create" to create the workspace. The deployment may take a few minutes to complete.
8. Access the Microsoft Defender for Cloud portal: Once the workspace is created, you can access the Microsoft Defender for Cloud portal by navigating to the resource group where you created the workspace. Select the Microsoft Defender for Cloud workspace, and in the overview page, click on "Go to workspace" to access the portal.
9. Configure additional settings and policies: Within the Microsoft Defender for Cloud portal, you can further configure settings and policies according to your organization's requirements. This includes configuring alerts, managing security policies, investigating incidents, and more.

*Creating Log Analytics Workspace*

To create a Log Analytics Workspace in Azure based on the given information, follow these steps:

1. Sign in to the Azure portal: Go to https://portal.azure.com and sign in using your Azure account credentials.
2. Navigate to Log Analytics: In the Azure portal, search for "Log Analytics" in the search bar. Select "Log Analytics workspaces" from the results.
3. Create a new Log Analytics Workspace: Click on the "+ Add" button to create a new workspace.
4. Configure workspace settings:
    - Subscription: Choose the Azure subscription where you want to create the Log Analytics Workspace.
    - Resource group: Select an existing resource group or create a new one to group your resources.
    - Workspace name: Provide a unique name for your Log Analytics Workspace.
    - Region: Choose the Azure region where you want to deploy the workspace.
    - Pricing tier: Select the appropriate pricing tier based on your requirements and budget.
5. Review and create the workspace: Review the configuration settings you have chosen for the Log Analytics Workspace. If everything looks correct, click on "Review + create" to proceed.
6. Configure advanced settings (optional): If you want to customize advanced settings, such as data retention, usage data collection, or Azure Monitor integration, you can click on the "Advanced" tab and make the desired configurations. Otherwise, you can leave the default settings.
7. Review and validate the settings: Review all the settings you have chosen for the workspace. Ensure that the information provided aligns with the given details, such as workspace name, region, and pricing tier.
8. Create the Log Analytics Workspace: Once you have reviewed and validated the settings, click on the "Create" button to create the Log Analytics Workspace. The deployment may take a few moments to complete.
9. Access the Log Analytics Workspace: After the workspace is successfully created, you can access it by navigating to the resource group where you created the workspace. Select the Log Analytics Workspace, and in the overview page, click on "Go to resource" to access the workspace.
10. Configure data sources and connect VMs: Within the Log Analytics Workspace, you can configure data sources to collect logs and connect virtual machines (VMs) to start collecting their logs. Follow the documentation provided by Azure to configure data sources and connect the VMs to the workspace.

 *Enabling Gathering VM Logs in Security Center To enable gathering VM logs in Azure Security Center based on the given information, follow these steps:*

1. Sign in to the Azure portal: Go to https://portal.azure.com and sign in using your Azure account credentials.
2. Navigate to Azure Security Center: In the Azure portal, search for "Security Center" in the search bar. Select "Security Center" from the results.
3. Choose the subscription and resource group: In the Security Center dashboard, select the Azure subscription and resource group that contains the virtual machine (VM) for which you want to enable log gathering.
4. Enable the "Log Collection" security control: In the Security Center dashboard, click on "Security controls" in the left-side menu. Scroll down and locate the "Log Collection" control. If it's not already enabled, click on the "Enable" button next to it.
5. Select the VM for log gathering: In the Log Collection control, you should see a list of your VMs. Locate the specific VM you want to enable log gathering for, and toggle the switch to "On" in the "Log Collection" column.
6. Review the log collection settings: After enabling log gathering for the VM, click on the "Review log collection settings" link next to the toggle switch. This will allow you to review and configure the specific logs that will be collected from the VM.
7. Configure the log collection settings: In the Log Collection settings, you can choose the types of logs you want to collect from the VM. Based on the given information, you may want to select relevant log types such as Event Logs, Syslog, or custom logs if applicable.
8. Save the log collection settings: After configuring the log collection settings, click on the "Save" button to save your changes.

*Connecting Log Analytics to VM To connect Log Analytics to a virtual machine (VM) in Azure, follow these steps:*

1. Sign in to the Azure portal: Go to https://portal.azure.com and sign in using your Azure account credentials.
2. Navigate to the virtual machine: In the Azure portal, search for "Virtual machines" in the search bar and select the appropriate VM from the results.
3. Enable diagnostic settings: In the VM's overview page, click on "Diagnostic settings" in the left-side menu.
4. Add diagnostic settings: Click on the "+ Add diagnostic setting" button to configure the diagnostic settings for the VM.
5. Configure diagnostic settings:
    - Diagnostic settings name: Provide a name for the diagnostic settings.
    - Logs: Enable the logs you want to collect from the VM. This can include system logs, application logs, security logs, etc.
    - Destination: Choose "Log Analytics" as the destination for the logs.
    - Log Analytics workspace: Select the Log Analytics workspace to which you want to connect the VM.
    - Save: Click on the "Save" button to save the diagnostic settings.
6. Verify the connection: Once the diagnostic settings are saved, the VM will start sending the specified logs to the Log Analytics workspace. You can verify the connection by navigating to the Log Analytics workspace and checking the "Logs" section to see if the logs from the VM are being collected.

*Setting up Azure Sentinel*

To set up Azure Sentinel, Microsoft's cloud-native Security Information and Event Management (SIEM) solution, follow these steps:

1. Sign in to the Azure portal: Go to https://portal.azure.com and sign in using your Azure account credentials.
2. Create an Azure Sentinel workspace: In the Azure portal, search for "Azure Sentinel" in the search bar and select "Azure Sentinel" from the results.
3. Create a new workspace: Click on the "+ Create" button to create a new Azure Sentinel workspace.
4. Configure workspace settings:
    - Subscription: Select the Azure subscription where you want to create the Azure Sentinel workspace.
     - Resource group: Choose the appropriate resource group or create a new one.
    - Workspace name: Provide a unique name for the Azure Sentinel workspace.
    - Region: Select the region where you want to deploy the workspace.
    - Pricing tier: Choose the pricing tier based on your requirements.
5. Review and create the workspace: Review the settings and click on the "Review + create" button. If everything looks good, click on the "Create" button to create the Azure Sentinel workspace.
6. Access the Azure Sentinel workspace: Once the workspace is created, navigate to the Azure Sentinel workspace in the Azure portal.
7. Connect data sources: In the Azure Sentinel workspace, click on "Data connectors" in the left-side menu. Select the data sources you want to connect to Azure Sentinel, such as Azure Active Directory, Azure Monitor, or Microsoft 365.
8. Enable analytics rules: In the Azure Sentinel workspace, click on "Analytics" in the left-side menu. Enable the pre-built analytics rules or create your own rules to detect specific security events and threats.
9. Customize workbooks and dashboards: In the Azure Sentinel workspace, click on "Workbooks" or "Dashboards" in the left-side menu to customize the visualizations and reports based on your security requirements.
10. Integrate threat intelligence: In the Azure Sentinel workspace, click on "Threat intelligence" in the left-side menu. Configure threat intelligence sources to enhance your threat detection capabilities.
11. Configure automation and response: In the Azure Sentinel workspace, click on "Automation" in the left-side menu. Create automation playbooks to automate response actions for detected security incidents.
12. Review and manage incidents: In the Azure Sentinel workspace, click on "Incidents" in the left-side menu. Review and manage the security incidents identified by Azure Sentinel.

*Logging into VM with Remote Desktop (Failed Logon) To log into a virtual machine (VM) using Remote Desktop and simulate a failed logon, follow these steps:*

1. Obtain the public IP address or DNS name of the VM: In the Azure portal, navigate to the virtual machine you want to log into. Note down the public IP address or DNS name associated with the VM.
2. Open the Remote Desktop client: On your local machine, open the Remote Desktop client application. This can usually be found by searching for "Remote Desktop" in the Start menu or using the Run dialog (press Win + R and type "mstsc").
3. Enter the VM's IP address or DNS name: In the Remote Desktop client, enter the public IP address or DNS name of the VM in the "Computer" field.
4. Configure additional settings (optional): Click on the "Show Options" button to expand the Remote Desktop client window and configure any additional settings, such as username, display resolution, or local resources.
5. Connect to the VM: Click on the "Connect" button to initiate the connection to the VM.
6. Enter the login credentials: In the Remote Desktop Connection window, enter the appropriate username and password for the VM.

*Observing Event Viewer Logs in VM To observe Event Viewer logs in a virtual machine (VM), follow these steps:*

1. Log into the VM: Use Remote Desktop or another method to log into the virtual machine.
2. Open Event Viewer: Once logged in, click on the Start menu, type "Event Viewer," and open the Event Viewer application.
3. Navigate to Event Logs: In the Event Viewer window, you will see a hierarchical structure on the left-hand side. Expand "Windows Logs" to access the different event logs available, such as Application, Security, Setup, System, etc.
4. Select an event log: Choose the event log you want to observe. For example, if you're interested in security-related events, select the "Security" log.
5. View event details: The selected event log will display a list of events with their corresponding details, including event ID, source, date, and time. Click on any event to view its full details.

*Turning off Windows Firewall on VM To turn off the Windows Firewall on a virtual machine (VM), follow these steps:*

1. Log into the VM: Use Remote Desktop or another method to log into the virtual machine.
2. Open the Windows Security settings:
3. Access the Windows Security app:
4. Open the Windows Security Firewall settings: In the Windows Security app, click on "Firewall & network protection" to access the firewall settings.
5. Turn off the Windows Firewall: Under the "Firewall & network protection" section, you will see different network profiles (e.g., Domain network, Private network, Public network). Click on each profile, and for each one, toggle the switch to "Off" to turn off the Windows Firewall.
6. Confirm the action: A warning message will appear, notifying you about the potential security risks of turning off the Windows Firewall. Confirm the action by clicking on "Yes" or "Turn off" to proceed.
7. Verify the Windows Firewall status: After turning off the Windows Firewall, you can verify its status by going back to the "Firewall & network protection" section in the Windows Security app. The firewall status for each network profile should show as "Off."

*Create PowerShell Script*
1. Open Power Shall :
2. Create New File :
3. Write a Script :

## Get API key from here: https://ipgeolocation.io/
$API_KEY = "Copy the key you get from ipgeolocation.io"  $LOGFILE_NAME = "failed_rdp.log" 
LOGFILEPATH="C:\ProgramData($LOGFILE_NAME)"
### This filter will be used to filter failed RDP events from Windows Event Viewer

`$XMLFilter = @' *[System[(EventID='4625')]] '@`

`<# This function creates a bunch of sample log files that will be used to train the Extract feature in Log Analytics workspace. If you don't have enough log files to "train" it, it will fail to extract certain fields for some reason -_-. We can avoid including these fake records on our map by filtering out all logs with a destination host of "samplehost" #> Function write-Sample-Log() { "latitude:47.91542,longitude:-120.60306,destinationhost:samplehost,username:fakeuser,sourcehost:24.16.97.222,state:Washington,country:United States,label:United States - 24.16.97.222,timestamp:2021-10-26 03:28:29" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:-22.90906,longitude:-47.06455,destinationhost:samplehost,username:lnwbaq,sourcehost:20.195.228.49,state:Sao Paulo,country:Brazil,label:Brazil - 20.195.228.49,timestamp:2021-10-26 05:46:20" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:52.37022,longitude:4.89517,destinationhost:samplehost,username:CSNYDER,sourcehost:89.248.165.74,state:North Holland,country:Netherlands,label:Netherlands - 89.248.165.74,timestamp:2021-10-26 06:12:56" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:40.71455,longitude:-74.00714,destinationhost:samplehost,username:ADMINISTRATOR,sourcehost:72.45.247.218,state:New York,country:United States,label:United States - 72.45.247.218,timestamp:2021-10-26 10:44:07" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:33.99762,longitude:-6.84737,destinationhost:samplehost,username:AZUREUSER,sourcehost:102.50.242.216,state:Rabat-Salé-Kénitra,country:Morocco,label:Morocco - 102.50.242.216,timestamp:2021-10-26 11:03:13" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:-5.32558,longitude:100.28595,destinationhost:samplehost,username:Test,sourcehost:42.1.62.34,state:Penang,country:Malaysia,label:Malaysia - 42.1.62.34,timestamp:2021-10-26 11:04:45" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:41.05722,longitude:28.84926,destinationhost:samplehost,username:AZUREUSER,sourcehost:176.235.196.111,state:Istanbul,country:Turkey,label:Turkey - 176.235.196.111,timestamp:2021-10-26 11:50:47" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:55.87925,longitude:37.54691,destinationhost:samplehost,username:Test,sourcehost:87.251.67.98,state:null,country:Russia,label:Russia - 87.251.67.98,timestamp:2021-10-26 12:13:45" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:52.37018,longitude:4.87324,destinationhost:samplehost,username:AZUREUSER,sourcehost:20.86.161.127,state:North Holland,country:Netherlands,label:Netherlands - 20.86.161.127,timestamp:2021-10-26 12:33:46" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:17.49163,longitude:-88.18704,destinationhost:samplehost,username:Test,sourcehost:45.227.254.8,state:null,country:Belize,label:Belize - 45.227.254.8,timestamp:2021-10-26 13:13:25" | Out-File $LOGFILE_PATH -Append -Encoding utf8 "latitude:-55.88802,longitude:37.65136,destinationhost:samplehost,username:Test,sourcehost:94.232.47.130,state:Central Federal District,country:Russia,label:Russia - 94.232.47.130,timestamp:2021-10-26 14:25:33" | Out-File $LOGFILE_PATH -Append -Encoding utf8 }`

### This block of code will create the log file if it doesn't already exist
`if ((Test-Path $LOGFILE_PATH) -eq $false) { New-Item -ItemType File -Path $LOGFILE_PATH write-Sample-Log }`

## Infinite Loop that keeps checking the Event Viewer logs.
`while ($true) {`

`Start-Sleep -Seconds 1`
`This retrieves events from Windows EVent Viewer based on the filter`
`$events = Get-WinEvent -FilterXml $XMLFilter -ErrorAction SilentlyContinue`
`if ($Error) {`
    `#Write-Host "No Failed Logons found. Re-run script when a login has failed."`
`}`
 `Step through each event collected, get geolocation`
   `for the IP Address, and add new events to the custom log`
`foreach ($event in $events) {`
    `# $event.properties[19] is the source IP address of the failed logon`
    `# This if-statement will proceed if the IP address exists (>= 5 is arbitrary, just saying if it's not empty)`
    `if ($event.properties[19].Value.Length -ge 5) {`

        ``# Pick out fields from the event. These will be inserted into our new custom log``
        ``$timestamp = $event.TimeCreated``
        ``$year = $event.TimeCreated.Year``

        ``$month = $event.TimeCreated.Month``
        ``if ("$($event.TimeCreated.Month)".Length -eq 1) {``
            ``$month = "0$($event.TimeCreated.Month)"``
        ``}``

        ``$day = $event.TimeCreated.Day``
        ``if ("$($event.TimeCreated.Day)".Length -eq 1) {``
            ``$day = "0$($event.TimeCreated.Day)"``
        ``}``
        
        ``$hour = $event.TimeCreated.Hour``
        ``if ("$($event.TimeCreated.Hour)".Length -eq 1) {``
            ``$hour = "0$($event.TimeCreated.Hour)"``
        ``}``

        ``$minute = $event.TimeCreated.Minute``
        ``if ("$($event.TimeCreated.Minute)".Length -eq 1) {``
            ``$minute = "0$($event.TimeCreated.Minute)"``
        ``}``


        ``$second = $event.TimeCreated.Second``
        ``if ("$($event.TimeCreated.Second)".Length -eq 1) {``
            ``$second = "0$($event.TimeCreated.Second)"``
        ``}``

        ``$timestamp = "$($year)-$($month)-$($day) $($hour):$($minute):$($second)"``
        ``$eventId = $event.Id``
        ``$destinationHost = $event.MachineName# Workstation Name (Destination)``
        ``$username = $event.properties[5].Value # Account Name (Attempted Logon)``
        ``$sourceHost = $event.properties[11].Value # Workstation Name (Source)``
        ``$sourceIp = $event.properties[19].Value # IP Address``
    

        ``# Get the current contents of the Log file!``
        ``$log_contents = Get-Content -Path $LOGFILE_PATH``

        ``# Do not write to the log file if the log already exists.``
        ``if (-Not ($log_contents -match "$($timestamp)") -or ($log_contents.Length -eq 0)) {``
        
            ``# Announce the gathering of geolocation data and pause for a second as to not rate-limit the API``
            ``#Write-Host "Getting Latitude and Longitude from IP Address and writing to log" -ForegroundColor Yellow -BackgroundColor Black``
            ``Start-Sleep -Seconds 1``

            ``# Make web request to the geolocation API``
            ``# For more info: https://ipgeolocation.io/documentation/ip-geolocation-api.html``
            ``$API_ENDPOINT = "https://api.ipgeolocation.io/ipgeo?apiKey=$($API_KEY)&ip=$($sourceIp)"``
            ``$response = Invoke-WebRequest -UseBasicParsing -Uri $API_ENDPOINT``

            ``# Pull Data from the API response, and store them in variables``
            ``$responseData = $response.Content | ConvertFrom-Json``
            ``$latitude = $responseData.latitude``
            ``$longitude = $responseData.longitude``
            ``$state_prov = $responseData.state_prov``
            ``if ($state_prov -eq "") { $state_prov = "null" }``
            ``$country = $responseData.country_name``
            ``if ($country -eq "") {$country -eq "null"}``

            ``# Write all gathered data to the custom log file. It will look something like this:``
            ``#``
            ``"latitude:$($latitude),longitude:$($longitude),destinationhost:$($destinationHost),username:$($username),sourcehost:$($sourceIp),state:$($state_prov), country:$($country),label:$($country) - $($sourceIp),timestamp:$($timestamp)" | Out-File $LOGFILE_PATH -Append -Encoding utf8``

            ``Write-Host -BackgroundColor Black -ForegroundColor Magenta "latitude:$($latitude),longitude:$($longitude),destinationhost:$($destinationHost),username:$($username),sourcehost:$($sourceIp),state:$($state_prov),label:$($country) - $($sourceIp),timestamp:$($timestamp)"``
        ``}``
        ``else {``
            ``# Entry already exists in custom log file. Do nothing, optionally, remove the # from the line below for output``
            ``# Write-Host "Event already exists in the custom log. Skipping." -ForegroundColor Gray -BackgroundColor Black``
        ``}``
    ``}``
`}`

*Obtaining Geolocation.io API Key*
To obtain an API key from Geolocation.io, which provides geolocation data, follow these steps:

1. Visit the Geolocation.io website: Go to the Geolocation.io website by entering "https://www.geolocation.io/" in your web browser.
2. Sign up for an account: Click on the "Sign Up" or "Get Started" button on the homepage to create a new account. You may need to provide your email address and create a password.
3. Verify your account: After signing up, you may receive a verification email from Geolocation.io. Follow the instructions in the email to verify your account.
4. Log in to your Geolocation.io account: Once your account is verified, go back to the Geolocation.io website and click on the "Login" or "Sign In" button. Enter your credentials to log in.
5. Access your API keys: After logging in, navigate to your account settings or profile section. Look for an option related to API keys or developer tools.
6. Generate a new API key: In the API keys or developer tools section, you should find an option to generate a new API key. Click on the appropriate button or link to create a new API key.
7. Copy your API key: Once the API key is generated, it should be displayed on the screen. Copy the API key to your clipboard or make note of it for future use.

*Running Script to Retrieve Geo Data of Attackers*
The provided code is a PowerShell script that continuously monitors the Windows Event Viewer logs for failed RDP logon events and retrieves the geolocation data of the attacker's IP address using the Geolocation.io API. It then writes the gathered data to a custom log file.

To run the script:

1. Open a PowerShell session: On your Windows machine, open PowerShell by searching for "PowerShell" in the Start menu or using the Run dialog (press Win + R and type "powershell").
2. Copy and paste the script into the PowerShell console.
3. Replace the placeholder API key ($API_KEY) with your actual Geolocation.io API key. You can obtain an API key by signing up for an account at https://ipgeolocation.io/.
4. Review the script and ensure that the log file path ($LOGFILE_PATH) is suitable for your environment. By default, it is set to "C:\ProgramData\failed_rdp.log", but you can modify it as needed.
5. Run the script by pressing Enter. The script will start monitoring the Windows Event Viewer logs for failed RDP logon events.
6. Whenever a new failed RDP logon event is detected, the script will retrieve the geolocation data for the attacker's IP address using the Geolocation.io API and append the gathered information to the log file.
7. The geolocation data, including latitude, longitude, destination host, username, source host, state/province, country, label, and timestamp, will be displayed in the PowerShell console.
8. The script will continue running indefinitely, continuously monitoring for new failed RDP logon events and updating the log file with the geolocation data.

*Creating Custom Log in Log Analytics Workspace*
To create a custom log in Log Analytics Workspace, you can follow these steps:

1. Sign in to the Azure portal (portal.azure.com) with your Azure account.
2. Navigate to your Log Analytics Workspace. You can search for "Log Analytics" in the Azure portal's search bar and select the Log Analytics service.
3. In the Log Analytics Workspace blade, click on "Advanced settings" in the left-hand menu.
4. Under the "Data" section, click on "Custom Logs".
5. Click on the "+ Add" button to create a new custom log.
6. In the "Add custom log" blade, provide the following information:
    - Log type name: Enter a unique name for your custom log.
    - Log files: Specify the log file or files that you want to ingest into the Log Analytics Workspace. You can provide a specific file path, use wildcards (*) to include multiple files, or use directories to include all files in a specific folder.
    - Log file format: Select the appropriate log file format from the available options. If your log file format is not listed, you can select "Other".
    - Timestamp field: Specify the field in your log file that represents the timestamp of each log entry.
    - Level fields: If your log file includes fields that represent log levels (e.g., "Information", "Warning", "Error"), you can specify those fields here.
    - Other fields: If your log file includes additional fields that you want to extract, you can specify them here. Enter the field name and its data type.
7. After providing the necessary information, click on the "Save" button to create the custom log.
8. Azure will start ingesting the specified log files into the Log Analytics Workspace based on the defined configuration. You can access and query the custom log data using Azure Monitor, Azure Log Analytics, or Azure Sentinel.

*Creating Custom Fields/Extracting Fields from Raw Custom Log Data*

To create custom fields or extract specific information from raw custom log data in Azure Log Analytics, you can use the Query Language (KQL) available in Azure Monitor. Here's a general approach to achieve this:
1. Navigate to the Azure portal (portal.azure.com) and open your Log Analytics Workspace.
2. Go to the "Logs" section in the Log Analytics Workspace.
3. 3.Identify the fields you want to extract or create. These can be existing fields in the log data or new fields that you want to generate based on the existing data.
*Testing Extracts*
*Setting up Map in Sentinel with Latitude and Longitude (or Country)*
- To set up a map visualization in Azure Sentinel using latitude and longitude or country data, you can follow these steps:
- Ensure that you have a Log Analytics Workspace connected to your Azure Sentinel instance.
 *Fixing Map Plot Sizes To adjust and optimize the map plot sizes in your Azure Sentinel workbook, you can follow these steps:
1. Open your workbook in the Azure Sentinel Workbooks section.
2. Locate the map visualization that you want to adjust.
3. Select the map visualization on the canvas, and you should see options appear on the right-hand side in the workbook designer.
4. Look for options such as "Map configuration" or "Map settings" and click on it to access the map customization options.
5. In the map configuration/settings, you should find options to adjust the plot sizes. The exact options available may vary depending on the visualization tool used within Azure Sentinel (e.g., Azure Maps, Kibana, Power BI, etc.).
6. Look for options related to marker size, circle size, or plot size, and adjust them according to your preference. You may be able to increase or decrease the size of the markers or circles representing the attack data points on the map.
7. Preview the changes as you make them to ensure that the plot sizes are visually appealing and effectively represent the data.
8. Save the workbook once you are satisfied with the adjusted map plot sizes.
9. Test the workbook by viewing the map visualization with the updated plot sizes to ensure that the attack data is displayed correctly and clearly.
10. Make further adjustments as needed until you achieve the desired map plot sizes and visual representation of the attack data.
 *Attack Scenario: China Begins Attacking*
In the attack scenario where China begins attacking, you can document the corresponding geolocation data as follows:
11. Capture Attack Data:
    - Monitor your SIEM system or event logs for incoming attack events originating from IP addresses associated with China.
    - Record the relevant attack details such as the source IP addresses, timestamps, attack types, and targeted systems.
12. Obtain Geolocation Data:
     -  Utilize the geolocation data retrieval mechanism you have set up to gather information about the attackers' IP addresses.
     -  Execute the PowerShell script or utilize the Geolocation.io API to retrieve the geolocation data for the identified IP addresses.
13. Store Geolocation Data:
    - Create a custom log in your Log Analytics Workspace to store the geolocation data specifically for the China-based attackers.
    - Ensure that the log includes fields such as the source IP address, geolocation information (latitude, longitude, country, etc.), and any other relevant details.
14. Populate the Custom Log:
    - Populate the custom log with the retrieved geolocation data for the attack events originating from China.
    - Each entry in the log should correspond to a specific attack event, containing the attack details and the associated geolocation information.
15. Analyze and Visualize the Data:
    - Utilize the capabilities of your SIEM system, such as Azure Sentinel, to analyze and visualize the geolocation data.
    - Use the latitude and longitude information to plot the attack events on a map visualization within your Azure Sentinel workbook.
    - Consider using other visualizations or filters to gain further insights into the attack patterns and their impact.
16. Document the Findings:
    - Document the findings and observations from the attack scenario involving China.
    - Include relevant details such as the frequency of attacks, targeted systems, attack types, and any notable patterns or trends.
    - Provide insights into the geolocation data, highlighting any concentrations or clusters of attack events in specific regions of China.
*Attack Scenario: Taiwan Joins the Attack*
In the attack scenario where Taiwan joins the attack, you can document the relevant geolocation data as follows:
17. Monitor Attack Events:
    - Continuously monitor your SIEM system or event logs for incoming attack events that originate from IP addresses associated with Taiwan.
    - Record the attack details such as the source IP addresses, timestamps, attack types, and targeted systems.
18. Retrieve Geolocation Data:
    - Utilize the geolocation data retrieval mechanism you have set up to obtain information about the attackers' IP addresses.
    - Execute the PowerShell script or use the Geolocation.io API to retrieve the geolocation data for the identified IP addresses.
19. Store Geolocation Data:
    - Create a custom log in your Log Analytics Workspace to store the geolocation data specifically for the attackers from Taiwan.
    - Ensure the log includes fields such as the source IP address, geolocation information (latitude, longitude, country, etc.), and any other relevant details.
20. Populate the Custom Log:
    - Populate the custom log with the retrieved geolocation data for the attack events originating from Taiwan.
    - Each entry in the log should correspond to a specific attack event, containing the attack details and the associated geolocation information.
21. Analyze and Visualize the Data:
    -  Utilize the capabilities of your SIEM system, such as Azure Sentinel, to analyze and   visualize the geolocation data.
    -  Use the latitude and longitude information to plot the attack events on a map visualization within your Azure Sentinel workbook.
    -  Consider using additional visualizations or filters to gain further insights into the attack patterns and their impact.
22. Document the Findings:
    -  Document the findings and observations from the attack scenario involving Taiwan.
    -  Include relevant details such as the frequency of attacks, targeted systems, attack types, and any notable patterns or trends.
    -  Provide insights into the geolocation data, highlighting any concentrations or clusters of attack events in specific regions of Taiwan.

*Create Python Script*
`import json`
`import datetime`
`import threading`
`#the file to be converted`
`filename = 'failed_rdp.txt'`
`#resultant dictionary`
`dict1 = {}`
`#fields in the sample file`
`#latitude:47.91542,longitude:-120.60306,destinationhost:samplehost,`
`#username:fakeuser,sourcehost:24.16.97.222,`
`#state:Washington,country:United States,`
`#label:United States - 24.16.97.222,timestamp:2021-10-26 03:28:29`
`fields =['latitude','longitude','destinationhost','username','sourcehost','state','country','label','timestamp']`
`with open(filename) as fh:`
    `# count variable for each attack id creation`
    `l = 1`
    `for line in fh:`
        `# reading line by line from the text file`
        `description = list( line.strip().split(None, 4))`
        `# for output see below`
        `print(description)`
        `# for automatic creation of attack id for each attack`
        `sno ='atck'+str(l)`
        `# loop variable`
        `i = 0`
        `# intermediate dictionary`
        `dict2 = {}`
        `while i<len(fields):`
                `# creating dictionary for each attacker details`
                `dict2[fields[i]]= description[i]`
                `i = i + 1`
        `# appending the record of each attacker to`
        `# the main dictionary`
        `dict1[sno]= dict2`
        `l = l + 1`
 `creating json file`      
`out_file = open("Jfailed_rdp.json", "w")`
`json.dump(dict1, out_file, indent = 9)`
`out_file.close()`
