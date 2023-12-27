from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Word(models.Model):
    word = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, through='WordCategory')

    def __str__(self):
        return self.word

class WordCategory(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.word} in {self.category} on {self.date}"

class DailyConnection(models.Model):
    date = models.DateField()
    words = models.ManyToManyField(WordCategory, related_name='daily_connections')
    categories_of_the_day = models.ManyToManyField(Category, related_name='daily_connections_of_the_day')

    def __str__(self):
        return f"Connections for {self.date}"

    

'''
from datetime import date
from yourapp.models import Category, Word, WordCategory, DailyConnection

# Assuming you have received data from NY Times
nyt_data = {
    "word1": ["category1", "category2"],
    "word2": ["category2", "category3"],
    # ... (up to word16)
    "word16": ["category15", "category16"],
}
categories_of_the_day = ["category_of_the_day1", "category_of_the_day2", "category_of_the_day3", "category_of_the_day4"]

# Step 1: Parse the data
today = date.today()

# Step 2: Create or retrieve Category instances
categories = {}
for category_name in set(categories_of_the_day):
    category, created = Category.objects.get_or_create(name=category_name)
    categories[category_name] = category

# Step 3: Create or retrieve Word instances with WordCategory relationships
words = {}
for word, category_names in nyt_data.items():
    word_instance, created = Word.objects.get_or_create(word=word)
    for category_name in category_names:
        word_category, created = WordCategory.objects.get_or_create(word=word_instance, category=categories[category_name], date=today)
    words[word] = word_instance

# Step 4: Create DailyConnection instance
daily_connection, created = DailyConnection.objects.get_or_create(date=today)

# Step 5: Associate the relevant WordCategory instances and categories with the DailyConnection
for word_instance in words.values():
    daily_connection.words.add(*WordCategory.objects.filter(word=word_instance, date=today))
for category in set(categories_of_the_day):
    daily_connection.categories_of_the_day.add(categories[category])

# Save the DailyConnection instance
daily_connection.save()
'''
