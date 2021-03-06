from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
import json
from datetime import date


class LastParameters(models.Model):
    """
    Model for storing preferences per user.
    """
    user = models.OneToOneField(User)
    parameters = JSONField()


def read_last_parameter(user, param, def_value=None):
    """
    Returns the last parameter for the user.

    :param user: the user to get the parameter for
    :type user: User
    :param param: the name of the parameter to retrieve
    :type param: str
    :param def_value: the default value to use
    :type def_value: str
    :return: the parameter value (or default value if not found)
    :rtype: str
    """
    params = LastParameters.objects.all().filter(user=user)
    result = def_value
    if len(params) > 0:
        jparams = json.loads(params[0].parameters)
        if param in jparams:
            result = jparams[param]
    return result


def write_last_parameter(user, param, value):
    """
    Saves the parameter value for the user.

    :param user: the user to save the parameter for
    :type user: User
    :param param: the name of the parameter to save
    :type param: str
    :param value: the value to store
    :type value: str
    """
    params = LastParameters.objects.all().filter(user=user)
    if len(params) == 0:
        p = LastParameters()
        p.user = user
        p.parameters = JSONField()
        jparams = json.loads("{}")
    else:
        p = params[0]
        jparams = json.loads(p.parameters)

    jparams[param] = value
    p.parameters = json.dumps(jparams)
    p.save()


class TableStatus(models.Model):
    """
    Status of tables.
    """
    table = models.CharField(max_length=250, db_index=True)
    timestamp = models.DateTimeField()
    message = models.TextField(null=True)

    class Meta:
        permissions = (
            ("can_access_table_status", "Can access Table Status"),
            ("can_manage_table_status", "Can manage Table Status"),
        )


class GradeResults(models.Model):
    """
    Grade results.

    Notes:
    - award_completion_year needs to be set to allow NULL values manually
    - NULL dates aren't possible, using "0001-01-01" instead
    """
    year = models.IntegerField(db_index=True, default=0)
    student_id = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    prefered_given_name = models.CharField(max_length=250, null=True, blank=True)
    given_name = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    other_given_names = models.CharField(max_length=250, null=True, blank=True)
    family_name = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    previous_name = models.CharField(max_length=250, null=True, blank=True)
    address1 = models.CharField(max_length=250, null=True, blank=True)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    address2a = models.CharField(max_length=250, null=True, blank=True)
    address2b = models.CharField(max_length=250, null=True, blank=True)
    address3 = models.CharField(max_length=250, null=True, blank=True)
    address4 = models.CharField(max_length=250, null=True, blank=True)
    postcode = models.CharField(max_length=250, null=True, blank=True)
    telephone = models.CharField(max_length=250, null=True, blank=True)
    cellphone = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    hasdisability = models.IntegerField(null=True)
    isdomestic = models.IntegerField(db_index=True, null=True)
    is_domiciled_locally = models.IntegerField(null=True)
    citizenship = models.CharField(max_length=250, null=True, blank=True)
    residency_status = models.CharField(max_length=250, null=True, blank=True)
    origin = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=250, null=True, blank=True)
    ethnicity = models.CharField(max_length=250, null=True, blank=True)
    ethnic_group = models.CharField(max_length=250, null=True, blank=True)
    all_ethnicities_string = models.CharField(max_length=250, null=True, blank=True)
    all_iwi_string = models.CharField(max_length=250, null=True, blank=True)
    dateofbirth = models.DateField(null=True)
    dateofdeath = models.CharField(max_length=250, null=True, blank=True)
    waikato_1st = models.IntegerField(null=True)
    nz_1st = models.IntegerField(null=True)
    last_year_sec = models.IntegerField(null=True)
    sec_qual_year = models.IntegerField(null=True)
    last_sec_school = models.CharField(max_length=250, null=True, blank=True)
    last_sec_school_region = models.CharField(max_length=250, null=True, blank=True)
    highest_sec_qual = models.CharField(max_length=250, null=True, blank=True)
    main_activity = models.CharField(max_length=250, null=True, blank=True)
    award_title = models.CharField(max_length=250, null=True, blank=True)
    prog_abbr = models.CharField(max_length=250, null=True, blank=True)
    programme = models.CharField(max_length=250, null=True, blank=True)
    programme_type_code = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    programme_type = models.CharField(max_length=250, null=True, blank=True)
    ishigherdegree = models.IntegerField(null=True)
    school_of_study = models.CharField(max_length=250, null=True, blank=True)
    school_of_study_clevel = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    paper_master_code = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    paper_occurrence = models.CharField(max_length=250, null=True, blank=True)
    paper_title = models.CharField(max_length=250, null=True, blank=True)
    occurrence_startdate = models.DateField(db_index=True, null=True)
    occurrence_startyear = models.IntegerField(db_index=True, null=True)
    occurrence_startweek = models.IntegerField(db_index=True, null=True)
    occurrence_enddate = models.DateField(db_index=True, null=True)
    stage = models.IntegerField(null=True)
    credits = models.FloatField(db_index=True, null=True)
    student_credit_points = models.FloatField(null=True)
    iscancelled = models.IntegerField(db_index=True, null=True)
    isoncampus = models.IntegerField(null=True)
    issemesteracourse = models.IntegerField(null=True)
    issemesterbcourse = models.IntegerField(null=True)
    iswholeyearcourse = models.IntegerField(null=True)
    location_code = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    owning_school_clevel = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    owning_school = models.CharField(max_length=250, null=True, blank=True)
    owning_department_clevel = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    owning_department = models.CharField(max_length=250, null=True, blank=True)
    owning_level4_clevel = models.CharField(max_length=250, null=True, blank=True)
    owning_level4_department = models.CharField(max_length=250, null=True, blank=True)
    owning_level4or3_department = models.CharField(max_length=250, null=True, blank=True)
    owning_level4or3_clevel = models.CharField(max_length=250, null=True, blank=True)
    delivery_mode_code = models.CharField(max_length=250, null=True, blank=True)
    delivery_mode = models.CharField(max_length=250, null=True, blank=True)
    semester_code = models.CharField(max_length=250, null=True, blank=True)
    semester_description = models.CharField(max_length=250, null=True, blank=True)
    isselfpaced = models.IntegerField(null=True)
    source_of_funding = models.CharField(max_length=250, null=True, blank=True)
    funding_category_code = models.CharField(max_length=250, null=True, blank=True)
    funding_category = models.CharField(max_length=250, null=True, blank=True)
    cost_category_code = models.CharField(max_length=250, null=True, blank=True)
    cost_category = models.CharField(max_length=250, null=True, blank=True)
    research_supplement_code = models.IntegerField(null=True)
    research_supplement = models.CharField(max_length=250, null=True, blank=True)
    classification_code = models.FloatField(null=True)
    classification = models.CharField(max_length=250, null=True, blank=True)
    division = models.CharField(max_length=250, null=True, blank=True)
    division_code = models.CharField(max_length=250, null=True, blank=True)
    specified_programme = models.CharField(max_length=250, null=True, blank=True)
    major = models.CharField(max_length=250, null=True, blank=True)
    second_major = models.CharField(max_length=250, null=True, blank=True)
    major2 = models.CharField(max_length=250, null=True, blank=True)
    second_major2 = models.CharField(max_length=250, null=True, blank=True)
    main_subject = models.CharField(max_length=250, null=True, blank=True)
    second_subject = models.CharField(max_length=250, null=True, blank=True)
    supporting_subject = models.CharField(max_length=250, null=True, blank=True)
    teaching_1 = models.CharField(max_length=250, null=True, blank=True)
    teaching_2 = models.CharField(max_length=250, null=True, blank=True)
    teaching_3 = models.CharField(max_length=250, null=True, blank=True)
    teaching_4 = models.CharField(max_length=250, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    field = models.CharField(max_length=250, null=True, blank=True)
    specialisation = models.CharField(max_length=250, null=True, blank=True)
    stream = models.CharField(max_length=250, null=True, blank=True)
    endorsement = models.CharField(max_length=250, null=True, blank=True)
    award_year = models.IntegerField(null=True)
    award_completion_status = models.CharField(max_length=250, null=True, blank=True)
    award_completion_date = models.DateField(null=True)
    award_completion_confirmed_date = models.DateField(null=True)
    admission_year = models.IntegerField(db_index=True, null=True)
    admission_reason = models.CharField(max_length=250, null=True, blank=True)
    admission_criteria = models.CharField(max_length=250, null=True, blank=True)
    admission_status = models.CharField(max_length=250, null=True, blank=True)
    grade = models.CharField(max_length=250, null=True, blank=True)
    grade_status = models.CharField(max_length=250, null=True, blank=True)
    result_status_code = models.CharField(max_length=250, null=True, blank=True)
    result_status = models.CharField(max_length=250, null=True, blank=True)
    grade_ranking = models.IntegerField(null=True)
    mark = models.FloatField(null=True)
    moe_completion_code = models.IntegerField(null=True)
    iscontinuinggrade = models.IntegerField(null=True)
    ispassgrade = models.IntegerField(null=True)
    query_date = models.DateField(null=True)
    enr_year = models.IntegerField(db_index=True, null=True)
    enrolment_status = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    final_grade = models.CharField(max_length=250, null=True, blank=True)
    final_grade_ranking = models.IntegerField(null=True)
    final_grade_status = models.CharField(max_length=250, null=True, blank=True)
    final_grade_result_status = models.CharField(max_length=250, null=True, blank=True)
    papers_per_student = models.IntegerField(null=True)
    credits_per_student = models.FloatField(null=True)
    gpa = models.FloatField(null=True)
    ones = models.IntegerField(null=True)
    allgradeones = models.IntegerField(null=True)
    passgradeones = models.IntegerField(null=True)
    retentionones = models.IntegerField(null=True)
    award_completion_year = models.IntegerField(db_index=True, null=True)
    personoid = models.FloatField(null=True)
    courseoccurrenceoid = models.FloatField(null=True)
    awardenrolmentoid = models.FloatField(null=True)
    enrolmentorcosuoid = models.FloatField(null=True)
    isformalprogramme = models.IntegerField(null=True)
    citizenship_simple = models.CharField(max_length=250, null=True, blank=True)
    moe_pbrf_code = models.CharField(max_length=250, null=True, blank=True)
    moe_pbrf = models.CharField(max_length=250, null=True, blank=True)
    achievement_date = models.DateField(null=True)
    te_reo = models.IntegerField(null=True)

    class Meta:
        permissions = (
            ("can_access_grade_results", "Can access Grade Results"),
            ("can_manage_grade_results", "Can manage Grade Results"),
        )


class CourseDefs(models.Model):
    """
    Course definitions.
    """
    year = models.IntegerField(db_index=True, default=0)
    code = models.CharField(db_index=True, max_length=20, default='')
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    type = models.CharField(db_index=True, max_length=50, default='')
    stage = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    delivery_mode = models.CharField(max_length=250, null=True)
    owning_programme = models.CharField(max_length=50, null=True)
    owning_programme_title = models.CharField(max_length=250, null=True)
    fw_level = models.IntegerField(null=True)
    hours_contact = models.IntegerField(null=True)
    hours_self_directed = models.IntegerField(null=True)
    hours_other_directed = models.IntegerField(null=True)
    funding_source = models.CharField(max_length=250, null=True)
    course_factor = models.FloatField(null=True)
    cost_category_code = models.CharField(max_length=20, null=True)
    cost_category = models.CharField(max_length=250, null=True)
    funding_class_code = models.CharField(max_length=20, null=True)
    funding_class = models.CharField(max_length=250, null=True)
    individual_efts = models.IntegerField(null=True)
    nzsced_code = models.CharField(max_length=20, null=True)
    nzsced_category = models.CharField(max_length=250, null=True)
    delivering_school_code = models.CharField(max_length=20, null=True)
    delivering_school = models.CharField(max_length=250, null=True)
    delivering_dept_code = models.CharField(max_length=20, null=True)
    delivering_dept = models.CharField(max_length=250, null=True)
    delivering_unit_code = models.CharField(max_length=20, null=True)
    delivering_unit = models.CharField(max_length=250, null=True)
    owning_school_code = models.CharField(max_length=20, null=True)
    owning_school = models.CharField(max_length=250, null=True)
    owning_dept_code = models.CharField(max_length=20, null=True)
    owning_dept = models.CharField(max_length=250, null=True)
    owning_unit_code = models.CharField(max_length=20, null=True)
    owning_unit = models.CharField(max_length=250, null=True)
    self_paced = models.NullBooleanField(null=True)
    online = models.NullBooleanField(null=True)
    active = models.NullBooleanField(null=True)
    pending = models.NullBooleanField(null=True)
    sub_status = models.CharField(max_length=20, null=True)
    grade_method_code = models.CharField(max_length=20, null=True)
    pbrf_eligibility = models.CharField(max_length=20, null=True)
    coe_policy = models.CharField(max_length=250, null=True)
    report_academic_result = models.NullBooleanField(null=True)
    internet_based = models.NullBooleanField(null=True)

    class Meta:
        permissions = (
            ("can_access_coursedefs", "Can access Course definitions"),
            ("can_manage_coursedefs", "Can manage Course definitions"),
        )


class Announcement(models.Model):
    """
    System-wide announcements.
    """

    TYPE_CHOICES = (
        ('s', 'Success'),
        ('i', 'Info'),
        ('w', 'Warning'),
        ('d', 'Danger'),
    )

    nickname = models.CharField(max_length=50, default='')
    text = models.TextField(default='')
    enabled = models.BooleanField(default=False)
    from_date = models.DateField(null=True, blank=True, default=None)
    to_date = models.DateField(null=True, blank=True, default=None)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='i')

    def __str__(self):
        return str(self.id) + "-" + str(self.nickname)


def get_active_announcements():
    """
    Returns a list of active announcements (each announcement is a dictionary).

    :return: the active accouncements
    :rtype: list
    """

    result = list()
    today = date.today()

    for a in Announcement.objects.all().filter(enabled=True):
        if a.from_date is not None:
            if today < a.from_date:
                continue
        if a.to_date is not None:
            if today > a.to_date:
                continue
        d = dict()
        d['text'] = a.text
        d['from_date'] = a.from_date
        d['to_date'] = a.to_date
        d['type'] = a.type
        result.append(d)

    return result
