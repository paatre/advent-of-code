import re                                                                                                    
                                                                                                             
with open('input.txt', encoding='utf-8') as file:                                                            
    lines = file.read().splitlines()                                                                         
    sum_of_game_ids = 0                                                                                      
    for line in lines:                                                                                       
        if line:                                                                                             
            game_id = re.findall("\d")[0]                                                                    
            sum_of_game_ids += game_id                                                                       
    print(sum_of_game_ids)
