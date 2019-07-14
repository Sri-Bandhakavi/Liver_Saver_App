# Liver_Saver_App 

An app that returns on demand liver injury risk labels for 2330 FDA approved drugs (includes all small molecule drugs approved before 2018). 

Liver injury risk labels returned by app are based on one of two sources: (1) FDA/Liver Toxicity Knowledge Base for 1036 drugs and (2) predicted liver injury risk labels for 1294 drugs based on logistic regression modeling using web-scraped real world evidence predictors from WHO/www.vigibase.org

App is based on Dash framework and can be implemented via running app.py along with csv file containing all drugs/liver injury risk labels.

Code (and datasets) used for predictive modeling of liver injury risk labels and combining with existing liver risk labels for limited drugs is available within the "modeling" folder.

