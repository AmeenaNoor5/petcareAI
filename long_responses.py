import random

# Existing responses
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

# Additional detailed responses for pet care
R_CARE_DOG = "To take care of a dog, make sure they have regular veterinary check-ups, a balanced diet, regular exercise, and plenty of love and attention. Keep their living area clean and provide them with mental stimulation and socialization opportunities."
R_CARE_CAT = "Cats need regular vet visits, a balanced diet, clean litter boxes, and plenty of enrichment and affection. Ensure they have a safe environment, plenty of toys, and scratching posts to keep them active and healthy."
R_SICK_DOG = "Common signs of a sick dog include changes in behavior, appetite, or energy levels, vomiting, diarrhea, coughing, and unusual discharge. If you notice any of these symptoms, it's best to consult your vet promptly."
R_SICK_CAT = "Look for signs like lethargy, changes in eating or drinking habits, hiding, vomiting, diarrhea, and respiratory issues. If your cat shows any of these symptoms, it's important to seek veterinary advice."
R_FEED_DOG = "A balanced diet for dogs includes high-quality commercial dog food or a vet-approved homemade diet. Ensure it has the right balance of protein, fats, and carbohydrates. Avoid giving them human food that can be toxic to dogs, like chocolate or onions."
R_FEED_CAT = "Cats need a diet high in protein and fat. High-quality commercial cat food or a vet-approved homemade diet is recommended. Avoid feeding them dog food or human foods that can be harmful, like chocolate, onions, or grapes."
R_TRAIN_DOG = "Training a dog involves consistent positive reinforcement, patience, and repetition. Start with basic commands like sit, stay, and come. Reward good behavior with treats and praise, and be consistent with your training sessions."
R_STOP_SCRATCHING_CAT = "Provide scratching posts, use deterrents on furniture, and keep your cat’s claws trimmed. You can also use pheromone sprays or covers on furniture to discourage scratching."
R_GROOM_DOG = "Regular grooming includes brushing their coat, trimming nails, cleaning ears, and occasional baths depending on the breed. Grooming helps to keep their coat healthy and can prevent health issues."
R_GROOM_CAT = "Brush your cat regularly, trim their nails, and ensure they have clean ears and teeth. Regular grooming helps to reduce shedding and prevents matting, especially in long-haired breeds."
R_DIARRHEA_DOG = "If your dog has diarrhea, ensure they stay hydrated, avoid giving food for 12 hours, then offer bland food like boiled chicken and rice. Consult your vet if it persists beyond 24 hours or if your dog shows other signs of illness."
R_COLD_CAT = "For a cat with a cold, keep them warm, ensure they stay hydrated, and consult your vet if symptoms persist beyond a few days. Provide a comfortable, quiet space for them to rest and recover."
R_FRUITS_DOG = "Dogs can eat fruits like apples (without seeds), blueberries, and bananas in moderation. Always remove seeds and cores and avoid giving them grapes or raisins as they are toxic to dogs."
R_CHOCOLATE_CAT = "Cats should not eat chocolate, onions, garlic, grapes, or raisins as they are toxic. Always keep these foods out of reach and ensure your cat has a diet appropriate for their nutritional needs."
R_BARKING_DOG = "To stop a dog from barking excessively, identify the cause, use positive reinforcement, and train commands like 'quiet'. Ensure they are getting enough exercise and mental stimulation, and address any potential sources of anxiety."
R_AGGRESSIVE_CAT = "If your cat is aggressive, ensure they have enough stimulation, use calming products, and consult your vet if needed. Identify any triggers for their aggression and create a safe environment for them to relax."
R_SHED_DOG = "For dogs that shed a lot, brush them frequently, use de-shedding tools, and consider a diet high in omega-3 fatty acids. Regular grooming helps manage shedding and keeps their coat healthy."
R_BATHE_CAT = "Bathe your cat only when necessary, use cat-specific shampoo, and ensure they are dried properly to avoid getting cold. Most cats groom themselves, so frequent baths are usually not needed."

# Unknown response
def unknown():
    response = [
        "Could you please re-phrase that?",
        "...",
        "Sounds about right.",
        "What does that mean?"
    ][random.randrange(4)]
    return response