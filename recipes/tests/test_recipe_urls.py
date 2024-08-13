from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RecipeURLsTest(TestCase):
    RECIPES_SERVER = "/recipes/"
    
    def test_the_pytest_is_ok(self):
        # print("Testando")
        assert 1 == 1
        

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, self.RECIPES_SERVER+"home/")
        
        
    def test_recipe_detail_url_is_correct(self):
        params = {"id": 2}
        url = reverse('recipes:detail', kwargs=params)
        self.assertEqual(url, self.RECIPES_SERVER+str(params['id'])+"/")