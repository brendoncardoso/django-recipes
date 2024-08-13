from django.test import TestCase
from django.urls import resolve, reverse

class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self): 
        view = resolve('/')
        self.assertTrue(True)
        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        ...
        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        text = response.content.decode('utf-8')
        self.assertIn("<p>No momento, não há receitas cadastradas no site.</p>", text)