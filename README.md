# Liver_Saver_App 

An app that returns on demand liver injury risk labels for 2330 FDA approved drugs (includes all small molecule drugs approved before 2018). 

Liver injury risk labels returned by app are based on one of two sources: (1) FDA/Liver Toxicity Knowledge Base for 1036 drugs and (2) predicted liver injury risk labels for 1294 drugs based on logistic regression modeling using web-scraped real world evidence predictors from www.vigibase.org and maintained by the world health organization's collaborating center for international drug monitoring.

Liver_Saver_App (https://liversaver1.herokuapp.com/) is based on the Python/Dash framework and can be implemented via running app.py along with csv file containing all drugs/liver injury risk labels. 

Python code (and datasets) used for predictive modeling of 1294 liver injury risk labels and combining with liver risk labels for 1036 drugs is available within the "modeling" folder.

