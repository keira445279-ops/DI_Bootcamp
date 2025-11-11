student_info = {'first_name':'Harry',
                'last_name': 'Potter',
                'age': [15, 10],
                'address':'Privet Drive, 4',
                'pets':['Hedwig', 'Buckbeak'],
                'best_friends': ('Ron Wealey', 'Hermione Granger'),
                'is_parselmouth': True,
                'houses': {'main': 'Griffyndor', 'second': 'Slytherin'}}

print (student_info ['age'])

student_info['address'] = 'Betzalel, 8'
print (student_info['address'])
student_info['pets'].append ('Leny')
print (student_info['pets'])
student_info['is_parselmouth'] = False
print(student_info['is_parselmouth'])


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print (sample_dict ["class"] ["student"] ["marks"] ["history"])