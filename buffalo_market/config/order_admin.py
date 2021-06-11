ADMIN_REORDER = (
    # Keep original label and models
    # 'sites',

    {'app': 'app_user',   'models': ('app_user.MyUser', 'app_user.Shop')},

    {'app': 'app_landmark','models': ('app_landmark.Landmark', )},
    {'app': 'app_purchase', 'models': ('app_purchase.ProductMockup', )},

    {'app': 'app_report', 'models': ('app_report.Products_Report','drf_api_logger.APILogsModel','app_report.Profile_Report' )},

    {'app': 'app_webconfig', 'models': ('app_webconfig.CategoryMockup',
                                        'app_webconfig.GroupFarmerMockup',
                                        'app_webconfig.ChoiceMockup',
                                        'app_webconfig.ProductStatusMockup',
                                        'drf_api.logger',
                                        )},

    {'app': 'app_location', 'models': ('app_location.GeographyMockup',
                                        'app_location.ProvinceMockup',
                                        'app_location.AmphurMockup',
                                        'app_location.DistrictMockup',)},
    # Rename app
    # {'app': 'ccc', 'label': 'Authorisation'},
    #
    # # # Reorder app models
    # {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
    #drf_api_logger
    # # Exclude models
    # {'app': 'auth', 'models': ('auth.User',)},
    #
    # # Cross-linked models
    # {'app': 'auth', 'models': ('auth.User', 'sites.Site')},
    #
    # models with custom name
    # {'app': 'app_user', 'models': (
    #     'auth.Group',
    #     {'model': 'auth.User', 'label': 'Staff'},
    # )},
)