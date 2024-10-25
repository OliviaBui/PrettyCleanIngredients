#This file does 4 things: 
## 1) It stores the 5x FDA-class allergen lists (as Dictionaries).
## 2) It cross-checks the allergen lists with pasted ingredients.
## 3) It indicates whether an allergen was detected (yes or no).
## 4) If yes, then it identifies and highlights the specific allergens from each category that triggered a warning for you to review.

#Building and storing allergens lists - Part 1
##Establishing dictionaries.
allergyDictionary = dict()

##Natural rubber allergens:
allergyDictionary["Natural rubbers"] = {"LATEX"}

##Fragrances allergens:
allergyDictionary["Fragrances"] = {"AMYL CINNAMAL","AMYLCINNAMYL ALCOHOL","ANISYL ALCOHOL","BENZYL ALCOHOL", "BENZYL BENZOATE", "BENZYL CINNAMATE", "BENZYL SALICYLATE" 
CINNAMYL ALCOHOL
CINNAMALDEHYDE
CITRAL
CITRONELLOL
COUMARIN
EUGENOL
FARNESOL
GERANIOL
HEXYL CINNAMALADEHYDE
HYDROXYCITRONELLAL
HYDROXYISOHEXYL 3-CYCLOHEXENE CARBOXALDEHYDE (HICC), (ALSO KNOWN AS LYRAL)
ISOEUGENOL
LILIAL
D-LIMONENE
LINALOOL
METHYL 2-OCTYNOATE
G-METHYLIONONE
OAK MOSS EXTRACT
"TREE MOSS EXTRACT"

#Preservatives allergens:
allergyDictionary["Preservatives"] = {"METHYLISOTHIAZOLINONE",
METHYLCHLOROISOTHIAZOLINONE 
BRONOPOL (2-BROMO-2-NITROPROPANE-1,3-DIOL)
5-BROMO-5-NITRO-1,3-DIOXANE
DIAZOLIDINYL UREA
DMDM HYDANTOIN (1,3-DIMETHYLOL-5,5-DIMETHYLHYDANTOIN)
IMIDAZOLIDINYL UREA
SODIUM HYDROXYMETHYLGLYCINATE
QUATERNIUM-15 (DOWICIL 200; N-(3-CHLOROALLYL) HEXAMINIUM CHLORIDE)}

#Dyes or colour additives allergens:
allergyDictionary["Dyes or colour additives"] = {"
p-phenylenediamine (PPD)
Coal-tar
"}

#Metals allergens
allergyDictionary["Metals"] = {"
Nickel
Gold"}

##Establishing the alternate listing of the allergens.
#Peanuts alternate listings:
allergyDictionary["Peanuts"] = {"ARTIFICAL NUTS","BEER NUTS","PEANUT OIL","COLD PRESSED PEANUT OIL","EXPELLER PRESSED PEANUT OIL","EXTRUDED PEANUT OIL","GOOBERS","GROUND NUTS","MIXED NUTS","MONKEY NUTS","NUT MEAT","PEANUT BUTTER","PEANUT FLOUR","PEANUT PROTEIN HYDROLYSATE", "PEANUTS", "PEANUT", "PEANUT BUTTER"}

#Sesame alternate listings:
allergyDictionary["Sesame"] = {"BENNE","BENNE SEED","BENNISEED","GINGELL","GINGELLY OIL","HALVAH","SESAME FLOUR","SESAME OIL","SESAME PASTE","SESAME SALT","SESAME SEED","SESAMOL","SESAMUM INDICUM","SESEMOLINA","SIM SIM","TAHINI","TAHINA","TEHINA","TIL"}

##Notes:
# isAllergic: the name of the yes/no detectkion function.
# ingredients: the list of copy-and-pasted user's ingredients like: {"Polybutene, Octyldodecanol", "Bis-Diglyceryl Polyacyladipate-2", "Tricaprylin"}
# allergySet: the list of selected categories they ticked like: {"fragrances", "preservatives", "metals")
# optionalAllergenset: customised added allergens list like: {"Maltodexrin"}
		# this one defaults to: set()
		# since it has the potential to be empty.

###Cross-checking user's data ('ingredients') with our data ('data.selectedAllergies'+'optionalAllergenSet') to flag for matches and result in a yes/no detection - Part 2
#We'll need to make 'ingredients' a list.
#We'll need to make the 'data.selectedAllergies' list to only pull from the allergens lists the user in interested in. 

def isAllergic(allergySet,ingredients,optionalAllergenSet = set()):
    for allergen in allergySet:
        if(len(ingredients)==1):
            for allergen in allergyDictionary[allergen]:
                if allergen in str(ingredients) and allergen!="BUTTER": return True
        else:
            for ingredient in ingredients:
                if(ingredient in allergyDictionary[allergen]) and ingredient!="BUTTER":
                    return True
                else:
                    for item in allergyDictionary[allergen]:
                        if item in ingredient and item!='BUTTER':
                            return True
    if(optionalAllergenSet!=set()):
        
        for optionAllergen in optionalAllergenSet:
            if(len(ingredients)==1):
                    if optionAllergen.upper() in str(ingredients): return True
            else:
                for ingredient in ingredients:
                    if(optionAllergen.upper() in ingredient):
                        return True
                    
                
    return False




###Highlighting the specific allergens + their respective categories - Part 3


#data.selectedAllergies is the allergy set, need to make ingredients into a list
def isAllergic(allergySet,ingredients,optionalAllergenSet = set()):
    for allergen in allergySet:
        if(len(ingredients)==1):
            for allergen in allergyDictionary[allergen]:
                if allergen in str(ingredients) and allergen!="BUTTER": return True
        else:
            for ingredient in ingredients:
                if(ingredient in allergyDictionary[allergen]) and ingredient!="BUTTER":
                    return True
                else:
                    for item in allergyDictionary[allergen]:
                        if item in ingredient and item!='BUTTER':
                            return True
    if(optionalAllergenSet!=set()):
        
        for optionAllergen in optionalAllergenSet:
            if(len(ingredients)==1):
                    if optionAllergen.upper() in str(ingredients): return True
            else:
                for ingredient in ingredients:
                    if(optionAllergen.upper() in ingredient):
                        return True
                    
                
    return False
    
    
    
def returnAllergen(allergySet,ingredients,optionalAllergenSet = set()):
    allergenList = []
    
    for allergen in allergySet:
        if(len(ingredients)==1):
            for allergen in allergyDictionary[allergen]:
                if allergen in str(ingredients):
                    if(allergen not in allergenList): 
                        allergenList.append(allergen)
        else:
            for ingredient in ingredients:
                if(ingredient in allergyDictionary[allergen]):
                    if(ingredient not in allergenList):
                        allergenList.append(ingredient)
                else:
                    for item in allergyDictionary[allergen]:
                        if item in ingredient:
                            if(item not in allergenList):
                                allergenList.append(item)
    if(optionalAllergenSet != set()):
        for optionalAllergen in optionalAllergenSet:
            if(len(ingredients)==1):
                    if optionalAllergen.upper() in str(ingredients): 
                        if(optionalAllergen not in allergenList):
                            allergenList.append(optionalAllergen)
            else:
                for ingredient in ingredients:
                    if(optionalAllergen.upper() in ingredient):
                        if(ingredient not in allergenList):
                            allergenList.append(ingredient)
                
                
    return allergenList