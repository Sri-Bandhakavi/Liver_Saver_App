# Liver_Saver_App 

An app (https://liversaver1.herokuapp.com/) that returns on demand liver injury risk labels for 2330 FDA approved drugs (includes all small molecule drugs approved before 2018). 

Liver injury risk labels returned by app are based on one of two sources: (1) FDA/Liver Toxicity Knowledge Base for 1035 drugs and (2) predicted liver injury risk labels for 1300 drugs based on best-in-class logistic regression model (balanced accuracy 79.5%) built from web-scraped real world evidence predictors (soource: www.vigibase.org; maintained by the world health organization's collaborating center for international drug monitoring).

Liver_Saver_App  is based on the Python/Dash framework and can be implemented via running app.py along with csv file containing 2330 drugs and associated liver injury risk labels. 

Python code (and datasets) used for predictive modeling of 1294 liver injury risk labels are available within the "modeling" folder.  For a youtube video describing this work, please see: https://www.youtube.com/watch?v=ZnXGmo27hDo


