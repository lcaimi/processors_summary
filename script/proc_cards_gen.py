import pandas as pd
# Informações faltantes na tabela
# - ISA modules
# - Nodes
# - TDP
# - Values of diferent columns 
#
#
#
#
# inicio do processamento da lista de processadores
df = pd.read_excel("../data/microarchitecture.xlsx", sheet_name=None)
#print(df)
#print(type(df))
#print(df.get("processors").keys())
html_text = "\t<body>\n\t\t<div id=\"cards\">\n" 
for i in range(72):
    fabric = df.get("processors").get("fabric").get(i)
    image_name = df.get("processors").get("Fig_name").get(i)
    codename = df.get("processors").get("Codename").get(i)
    released = df.get("processors").get("Released").get(i)
    threads = df.get("processors").get("Threads_core").get(i)
    decode_rate = df.get("processors").get("Peak_Decod_ Rate").get(i)  #Peak Decode Rate
    dispatch_rate = df.get("processors").get("Peak_Dispatch_Rate").get(i)  #Peak Dispatch Rate
    issue_rate = df.get("processors").get("Peak_Issue_Rate").get(i)  #
    retire_rate = df.get("processors").get("Retire_Rate").get(i)  #Retire Rate
    execution_ports = df.get("processors").get("Execution_Ports").get(i)  #Execution Ports
    decode_queue_entries = df.get("processors").get("Decode_Queue_Entries").get(i)  #Reorder Buffer Entrie
    reorder_buffer_entries = df.get("processors").get("Reorder_Buffer_Entries").get(i)  #
    total_scheduler_entries = df.get("processors").get("Total_Scheduler_Entries").get(i)  #Total Scheduler Entries
    store_queue_entries = df.get("processors").get("Store_Queue_Entries").get(i)  #Store Queue Entries
    load_queue_entries = df.get("processors").get("Load_Queue_Entries").get(i)  #Load Queue Entries
    microOp_cache = df.get("processors").get("MicroOp_Cache").get(i)  #
    L1_Icache = df.get("processors").get("L1_Icache").get(i)  #L1 I Cache
    L1_Dcache = df.get("processors").get("L1_Dcache").get(i)  #L1 D Cache
    L2_Cache = df.get("processors").get("L2_Cache").get(i)  #L2 Cache
    L3_Cache = df.get("processors").get("L3_Cache").get(i)  #L3 Cache
    L1_D_Latency = df.get("processors").get("L1_D_Latency").get(i)  #L1 D Cache Latency
    #L1_I_Latency = df.get("processors").get("L1_I_Latency").get(i)  #L1 I Cache Latency
    L2_Latency = df.get("processors").get("L2_Latency").get(i)  #L2 Cache Latency
    L3_Latency = df.get("processors").get("L3_Latency").get(i)  #L3 Cache Latency
    estimated_IPC_single = df.get("processors").get("Estimated_IPC_Single").get(i)  #Estimated IPC (Single Thread)
    estimated_IPC_hyper = df.get("processors").get("Estimated_IPC_Hyper").get(i)  #Estimated IPC (Hyperthread)
    ISA = df.get("processors").get("ISA").get(i)  #ISA
    node = df.get("processors").get("Node").get(i)  #Node
    power = df.get("processors").get("power").get(i)  #Power

    html_text += "\t\t\t<figure class=\"card card--" 
    if fabric == "Intel":
       html_text += "water\">\n"
    if fabric == "AMD":
       html_text += "fire\">\n"
    if fabric == "ARM":
       html_text += "psychic\">\n"    
    if fabric == "Apple":
       html_text += "grass\">\n"  
    if fabric == "Ampere":
       html_text += "dark\">\n"                 

    html_text += "\t\t\t\t<div class=\"card__image-container\">\n"
    html_text += "\t\t\t\t\t<a href=\"./images/" + str(image_name) + "\" target=\"_blank\">\n"
    html_text += "\t\t\t\t\t\t<img src=\"./images/" + str(image_name) + "\"  width=\"250\" height=\"320\" alt=\"Eevee\" class=\"card__image\">\n"
    html_text += "\t\t\t\t\t</a>\n"
    html_text += "\t\t\t\t</div>\n"
    html_text += "\t\t\t\t<figcaption class=\"card__caption\">\n"
    html_text += "\t\t\t\t\t<h1 class=\"card__name\">" + str(fabric) + " (" + str(codename) +") </h1>\n"
    html_text += "\t\t\t\t\t<h3 class=\"card__type\">" + str(released) + "</h3>\n"

    html_text += "\t\t\t\t\t<div class=\"battery\">\n"
    html_text += "\t\t\t\t\t\t<h3 class=\"battery-level "
    if power == "Very Low":
       html_text += "normal"    
    if power == "Low":
       html_text += "warn"
    if power == "High":
       html_text += "alert"
    html_text += "\" style=\"height:100%;\">" + str(power) + "</h3>\n"
    html_text += "\t\t\t\t\t</div>\n"

    html_text += "\t\t\t\t\t<table class=\"card__stats\">\n"
    html_text += "\t\t\t\t\t\t<tbody>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Threads:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td>" + str(threads) + "</td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Peak Decode Rate:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td>" + str(decode_rate) + "</td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Decode Queue Entries:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(decode_queue_entries) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"    

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>MicroOp Cache:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(microOp_cache) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"    

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Peak Dispatch Rate:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(dispatch_rate) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Reorder Buffer Entries:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(reorder_buffer_entries) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Total Scheduler Entries:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(total_scheduler_entries) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Execution Ports:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td>" + str(execution_ports) + "</td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Load Queue Entries:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(load_queue_entries) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Store Queue Entries:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(store_queue_entries) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Retire Rate:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(retire_rate) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L1 I Cache (KB):</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(L1_Icache) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L1 D Cache (KB):</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td>" + str(L1_Dcache) + "</td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L2 Cache (KB):</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(L2_Cache) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L3 Cache (KB):</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(L3_Cache) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L1 D Cache Latency:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(L1_D_Latency) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L2 Cache Latency:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(L2_Latency) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>L3 Cache Latency:</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(L3_Latency) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Estimated IPC (Single Thread):</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(estimated_IPC_single) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t\t<tr>\n"
    html_text += "\t\t\t\t\t\t\t\t<th>Estimated IPC (Hyperthread):</th>\n"
    html_text += "\t\t\t\t\t\t\t\t<td> " + str(estimated_IPC_hyper) + " </td>\n"
    html_text += "\t\t\t\t\t\t\t</tr>\n"

    html_text += "\t\t\t\t\t\t</tbody>\n\t\t\t\t\t</table>\n"
    html_text += "\t\t\t\t\t<div class=\"card__abilities\">\n"
    html_text += "\t\t\t\t\t\t<h4 class=\"card__ability\">\n"
    html_text += "\t\t\t\t\t\t\t<span class=\"card__label\">ISA</span>\n"
    html_text += "\t\t\t\t\t\t\t\t" + str(ISA) + "\n"
    html_text += "\t\t\t\t\t\t</h4>\n"
    html_text += "\t\t\t\t\t\t<h4 class=\"card__ability\">\n"
    html_text += "\t\t\t\t\t\t\t<span class=\"card__label\">Node</span>\n"
    html_text += "\t\t\t\t\t\t\t" + str(node) + "\n"
    html_text += "\t\t\t\t\t\t</h4>\n"
    html_text += "\t\t\t\t\t</div>\n"
    html_text += "\t\t\t\t</figcaption>\n"
    html_text += "\t\t\t</figure>\n"
html_text += "\t\t</div>\n"
html_text += "\t</body>\n"
html_text += "</html>\n"

print(html_text)
