from django.shortcuts import render

# Create your views here.
def recipe_list(request):
    lr = {
            "recipes": [
                {
                    "name": "Recipe 1",
                    "ingredients": [
                        {
                            "name": "tomato",
                            "quantity": "3pcs"
                        },
                        {
                            "name": "onion",
                            "quantity": "1pc"
                        },
                        {
                            "name": "pork",
                            "quantity": "1kg"
                        },
                        {
                            "name": "water",
                            "quantity": "1L"
                        },
                        {
                            "name": "sinigang mix",
                            "quantity": "1 packet"
                        }
                    ],
                    "link": "/recipe/1"
                },
                {
                    "name": "Recipe 2",
                    "ingredients": [
                        {
                            "name": "garlic",
                            "quantity": "1 head"
                        },
                        {
                            "name": "onion",
                            "quantity": "1pc"
                        },
                        {
                            "name": "vinegar",
                            "quantity": "1/2cup"
                        },
                        {
                            "name": "water",
                            "quanity": "1 cup"
                        },
                        {
                            "name": "salt",
                            "quantity": "1 tablespoon"
                        },
                        {
                            "name": "whole black peppers",
                            "quantity": "1 tablespoon"
                        },
                        {
                            "name": "pork",
                            "quantity": "1 kilo"
                        }
                    ],
                    "link": "/recipe/2"
                }
        ]
    }

    return render(request, 'recipe_list.html', lr)


def recipe_1(request):
    r1 = {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
    }

    return render(request, 'recipe_1.html', r1)


def recipe_2(request):
    r2 = {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
    }


    return render(request, 'recipe_2.html', r2)