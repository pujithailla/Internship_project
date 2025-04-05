def chatbot():
    steps = {}
    steps[1] = ["Sedan", "SUV", "Hatchback"]
    steps[2] = {"Sedan": ["Toyota Camry", "Honda Civic", "Hyundai Elantra"],
                "SUV": ["Honda CR-V", "Toyota RAV4", "Mazda CX-5"],
                "Hatchback": ["Honda Fit", "Hyundai Accent", "Kia Rio"]}
    steps[3] = {"Toyota Camry": ["2023", "2022", "2021"],
                "Honda Civic": ["2023", "2022", "2021"],
                "Hyundai Elantra": ["2023", "2022", "2021"],
                "Honda CR-V": ["2023", "2022", "2021"],
                "Toyota RAV4": ["2023", "2022", "2021"],
                "Mazda CX-5": ["2023", "2022", "2021"],
                "Honda Fit": ["2023", "2022", "2021"],
                "Hyundai Accent": ["2023", "2022", "2021"],
                "Kia Rio": ["2023", "2022", "2021"]}
    steps[4] = {"2023": ["Red", "Blue", "Black"],
                "2022": ["Silver", "White", "Gray"],
                "2021": ["Green", "Brown", "Beige"]}
    steps[5] = {"Red": ["Leather", "Cloth"],
                "Blue": ["Leather", "Cloth"],
                "Black": ["Leather", "Cloth"],
                "Silver": ["Leather", "Cloth"],
                "White": ["Leather", "Cloth"],
                "Gray": ["Leather", "Cloth"],
                "Green": ["Leather", "Cloth"],
                "Brown": ["Leather", "Cloth"],
                "Beige": ["Leather", "Cloth"]}
    steps[6] = {"Leather": {"Toyota Camry": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                            "Hyundai Accent": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                            "Honda Fit": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                            "Kia Rio": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                            "Mazda CX-5": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                            "Honda CR-V": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                            "Hyundai Elantra": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                           "Honda Civic": {}}, # ...add prices for other models
                "Cloth":  {"Toyota Camry": {"2023": {"Red": 15000, "Blue": 19000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 27000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                          "Honda Civic": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                     "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                     "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                          "Mazda CX-5": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                    "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                    "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                          "Honda CR-V": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                    "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                    "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                          "Hyundai Elantra": {"2023": {"Red": 30000, "Blue": 29000, "Black": 31000},
                                    "2022": {"Silver": 27000, "White": 28000, "Gray": 26000},
                                    "2021": {"Silver": 67000, "White": 17000, "Gray": 24000}},
                          "Kia Rio": {}}}


    current_step = 1
    user_choices = {}

    while current_step <= 6:
        print(f"\nStep {current_step}:")
        options = steps.get(current_step)
        if current_step == 1:
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
        elif current_step == 2 or current_step == 3 or current_step == 4 or current_step == 5:
           
            for i, option in enumerate(options.get(user_choices.get(current_step - 1))):
                print(f"{i + 1}. {option}")
        elif current_step == 6:
            car_model = user_choices.get(2)
            year = user_choices.get(3)
            color = user_choices.get(4)
            interior = user_choices.get(5)
            try:
                price = steps[6][interior][car_model][year][color]
                print(f"The price for car {car_model}, from year {year}, with color {color}, having {interior} interior costs ${price}")
                break
            except KeyError:
                print(f"Sorry price not available for this configuration")
                break 
                
        choice = input(f"Enter your choice (or '0' to go back): ")

        if choice.lower() == '0':
            if current_step > 1:
                current_step -= 1
            else:
              print("You are at the first step!")
        elif choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                if current_step == 1:
                    user_choices[current_step] = options[choice_num - 1]
                elif current_step == 2 or current_step == 3 or current_step == 4 or current_step == 5 :
                    previous_choice = user_choices.get(current_step-1)
                    available_options = options.get(previous_choice)
                    user_choices[current_step] = available_options[choice_num-1]
                
                current_step += 1
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number or 'b'.")

chatbot()
