import re
import json

def parse_data(annotation_path, output_path):

    data = {}

    current_user = None
    current_word = None

    global itr 
    itr = 0

    with open(annotation_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Remove leading/trailing whitespace
        line = line.strip()  
        num = ''
        try :
            num = int(line[0])
        except:
            pass
        numerical_lines = line.split()
        if line.startswith("User:"):
            itr = 0
            current_user = line.split()[1].strip()  
             

            # current_word = line.split(":")[1].strip()  
            line_data = line.split()
            current_word = line_data[len(line_data)-1]
            start_match = re.search('W', current_word)
            end_match = re.search('F', current_word)
            extracted_word = current_word[start_match.end(0):end_match.start(0)]
            word_name = 'W'+extracted_word
            orientation = line_data[3]
            fileName = line_data[11] 
            if current_user is not None:
                
                temp = {
                    "User": current_user,
                    "Orientation": orientation,  
                    "Session": line_data[5],
                    "View": line_data[7],
                    "FrameRate": line_data[9],
                    "FileName": fileName,
                    "no_of_trials": 0,
                    "trials": {} 
                }
                try:
                    data[word_name]
                except:
                    data[word_name] = {}
                try:
                    data[word_name][current_user] 
                except:
                    data[word_name][current_user]={}
                try:
                    data[word_name][current_user][orientation] 
                except:
                    data[word_name][current_user][orientation]={}
                try:
                    data[word_name][current_user][orientation][fileName] 
                except:
                    data[word_name][current_user][orientation][fileName] ={}
                data[word_name][current_user][orientation][fileName] =temp
        elif line.startswith("trials:"):
            if current_user is not None and word_name is not None:
                trials_count =(line.split(":")[1].strip())  
                data[word_name][current_user][orientation][fileName]["no_of_trials"] = trials_count
                print(line)
        elif isinstance(num, int):
            print(annotation_path)
            print("Hola",line)
            line_parts = (line.split('/')[1]).split()
            starting = int(line_parts[0])
            ending = int(line_parts[1])
            if (ending -starting) >=12:
                starting = starting + 2
                ending = ending - 2
            print(starting,ending)
            
            # starting = line_parts[1]
            # ending = line_parts[2]
            # # temp_dict = {trail_no : {'starting' : starting, 'ending' : ending }}
            data[word_name][current_user][orientation][fileName]["trials"][itr] = {'starting' : starting, 'ending' : ending }
            itr += 1

    #update the no_trials field as that is sometimes missing or wrong    
    for word in data:
        for user in data[word]:
            for orientation in data[word][user]:
                for fileName in data[word][user][orientation]:                                      
                    no_trials = len(data[word][user][orientation][fileName]['trials'])
                    data[word][user][orientation][fileName]['no_of_trials']= no_trials

    json_data = json.dumps(data, indent=4)


    with open(f'{output_path}/output1.json', 'w') as json_file:
        json_file.write(json_data)