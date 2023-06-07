from django.db import models

class BajajAllianzGroupSampoornaJeevanSuraksha(models.Model):
    '''
    Model for Bajaj Allianz Group Sampoorna Jeevan Suraksha policy
    '''
    min_sum_assured = models.IntegerField()
    max_sum_assured = models.IntegerField()
    min_age_limit = models.IntegerField()
    max_age_limit = models.IntegerField()
    policy_tenure_ranges = models.CharField(max_length=200, blank=True, null=True)
    sum_assured_ranges = models.CharField(max_length=200, blank=True, null=True)
    annual_income_threshold = models.IntegerField()
    otp_authentication = models.BooleanField()
    spouse_coverage_eligible = models.BooleanField()

    def __str__(self):
        return self.min_sum_assured