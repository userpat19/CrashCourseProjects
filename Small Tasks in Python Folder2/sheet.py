

def file_seeker():
   
   total = 0.0

   try:

        file_path = "none.txt"

        file = open(file_path, "r")

        for line in file:
            amount = float(line)
            total += amount

        print(total)

        file.close()

   except IOError:
       print("File was not found")

   except ValueError:
       print("Value error occured")

   except:
       print("There was an error")
   

    


file_seeker()

