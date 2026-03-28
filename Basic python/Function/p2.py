data = [" robiul ","","hasan","jisan",None,"  ","asif"]

clean_data = list (
    map(lambda x : x.strip(),filter(lambda x: x and x.strip(),data)))

print(clean_data)