from django.db import models

# Create your models here.

SOCIAL_ICON = (
    ('fa fa-github', 'fa fa-github'),
    ('fa fa-linkedin-square', 'fa fa-linkedin-square'),
    ('fa fa-facebook-official', 'fa fa-facebook-official'),
    ('fa fa-instagram', 'fa fa-instagram'),
    ('fa fa-codepen', 'fa fa-codepen'),
    ('fa fa-google-plus-official', 'fa fa-google-plus-official'),
    ('fa fa-jsfiddle', 'fa fa-jsfiddle'),
    ('fa fa-medium', 'fa fa-medium'),
    ('fa fa-pinterest', 'fa fa-pinterest'),
    ('fa fa-quora', 'fa fa-quora'),
    ('fa fa-reddit', 'fa fa-reddit'),
    ('fa fa-scribd', 'fa fa-scribd'),
    ('fa fa-snapchat', 'fa fa-snapchat'),
    ('fa fa-skype', 'fa fa-skype'),
    ('fa fa-slideshare', 'fa fa-slideshare'),
    ('fa fa-slack', 'fa fa-slack'),
    ('fa fa-stack-overflow', 'fa fa-stack-overflow'),
    ('fa fa-telegram', 'fa fa-telegram'),
    ('fa fa-twitter', 'fa fa-twitter'),
    ('fa fa-tumblr-square', 'fa fa-tumblr-square'),
    ('fa fa-whatsapp', 'fa fa-whatsapp'),
    ('fa fa-wordpress', 'fa fa-wordpress'),
    ('fa fa-yahoo', 'fa fa-yahoo'),
    ('fa fa-youtube', 'fa fa-youtube'),

)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),

)


class Intro(models.Model):
    img = models.ImageField(upload_to="images/", verbose_name="Set a portfolio image", null=True, blank=True)
    exp = models.PositiveIntegerField(null=True, verbose_name="Experience (Years)", blank=True)
    name = models.CharField(max_length=200, verbose_name="Enter your Name", blank=True)
    d_o_b = models.DateField(verbose_name="Date of Birth", blank=True)
    e_mail = models.EmailField(verbose_name="Email ID", blank=True)
    contact = models.CharField(max_length=10, verbose_name="Contact No. :", blank=True)
    city = models.CharField(max_length=100, verbose_name="Enter city", blank=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default="Male", blank=True)
    resume = models.FileField(upload_to="media/files/", null=True, blank=True)
    tagline = models.CharField(max_length=200, null=True, verbose_name="Do you want to add a tagline ", blank=True)
    desc = models.TextField(verbose_name="Describe yourself", null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Introduction'


class education(models.Model):
    is_show = models.BooleanField(verbose_name="Tick if you want to show it on portfolio")
    name1 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100, verbose_name="Enter your qualification (10h,12th,"
                                                                  "BCA,MCA etc)", null=True, blank=True)
    institute = models.CharField(max_length=300, verbose_name="Institute Name", null=True)
    Affiliated_to = models.CharField(max_length=200, verbose_name="Affiliated to (CBSE,GGISPU,SHARDA etc)", null=True,
                                     blank=True)
    is_pursuing = models.BooleanField(verbose_name=" True if Pursuing")
    Year_pass = models.CharField(max_length=4, verbose_name="Year of passing", null=True, blank=True)
    Result = models.CharField(max_length=5, verbose_name="Enter the result (percentage ,CGPA)", null=True, blank=True)

    def __str__(self):
        return str(self.qualification)

    class Meta:
        verbose_name = 'Education'


class key_specialization(models.Model):
    is_show1 = models.BooleanField(verbose_name="Tick if you want to show it on portfolio")
    name2 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    specialization_in = models.CharField(max_length=200, verbose_name="Enter the technology in which you are "
                                                                      "specialized", null=True, blank=True)

    def __str__(self):
        return str(self.specialization_in)

    class Meta:
        verbose_name = 'Key Specialization'


class certification(models.Model):
    is_show2 = models.BooleanField(verbose_name="Tick if you want to show it on portfolio")
    img3 = models.ImageField(upload_to="images/", verbose_name="Do you want Set a  image", null=True, blank=True)
    name3 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=100, verbose_name="Got certificate in", null=True, blank=True)
    certificate_from = models.CharField(max_length=200, verbose_name="Got certificate from", null=True, blank=True)
    Certificate_on = models.DateField(auto_now=True, verbose_name="Certificate got on", null=True, blank=True)
    certificate_url = models.URLField(verbose_name="Any URL of certificate or anything", null=True, blank=True)

    def __str__(self):
        return str(self.certificate_name)

    class Meta:
        verbose_name = 'My Certificate'


class key_achievements(models.Model):
    is_show3 = models.BooleanField(verbose_name="Tick if you want to show it on portfolio")
    name4 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    achievement_in = models.CharField(max_length=1000, verbose_name="Enter your achievements", null=True, blank=True)

    def __str__(self):
        return str(self.achievement_in)

    class Meta:
        verbose_name = 'Key Achievement'


class skill(models.Model):
    name5 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    skill_in = models.CharField(max_length=1000, verbose_name="Enter the list of  your skill", null=True, blank=True)

    def __str__(self):
        return str(self.skill_in)

    class Meta:
        verbose_name = 'My Skill'


class trait(models.Model):
    name6 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    traits_in = models.CharField(max_length=1000, verbose_name="Enter the list of  your traits", null=True, blank=True)

    def __str__(self):
        return str(self.traits_in)

    class Meta:
        verbose_name = 'My Trait'


class projects(models.Model):
    is_show4 = models.BooleanField(verbose_name="Tick if you want to show it on portfolio")
    img7 = models.ImageField(upload_to="images/", verbose_name="Do you want Set a  image", null=True, blank=True)
    name7 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200, verbose_name="Enter the tittle for your project", null=True,
                                    blank=True)
    project_tech = models.CharField(max_length=300, verbose_name="Main Technology used in your project", null=True,
                                    blank=True)
    software = models.CharField(max_length=500, verbose_name="List the key software(python,flask,selenium etc)",
                                null=True, blank=True)
    proj_url = models.URLField(verbose_name="Do you want to add a link of your project like git or any other",
                               blank=True)
    proj_desc = models.TextField(verbose_name="Project description", null=True, blank=True)
    is_upcoming = models.BooleanField(verbose_name="Tick if you are planning or starting to work on it")
    is_work = models.BooleanField(verbose_name="Tick if you are working on it")
    start_date = models.DateField(verbose_name="Started project on", null=True, blank=True)
    end_date = models.DateField(verbose_name="Project ended on", null=True, blank=True)

    def __str__(self):
        return str(self.project_name)

    class Meta:
        verbose_name = 'My Project'


class social_url(models.Model):
    is_show5 = models.BooleanField(verbose_name="Tick if you want to show it on portfolio")
    name8 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    class_icon = models.CharField(max_length=200, choices=SOCIAL_ICON, null=True)
    url_link = models.URLField(verbose_name="any social URL link (facebook,github,linkedin,instagram etc)", null=True,
                               blank=True)

    def __str__(self):
        return str(self.class_icon)

    class Meta:
        verbose_name = 'My Social URL'


class query(models.Model):
    query_name = models.CharField(max_length=300, verbose_name="Enter your name")
    query_email = models.EmailField(verbose_name="Your E mail ID")
    query_contact = models.CharField(max_length=10, verbose_name="Enter your phone number", null=True, blank=True)
    query_desc = models.TextField(verbose_name="Write your query")

    def __str__(self):
        return str(self.query_name)

    class Meta:
        verbose_name = ' Query'


class internships(models.Model):
    is_show6 = models.BooleanField(verbose_name="Tick if  you want to show it on portfolio")
    name9 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    c_img1 = models.ImageField(upload_to="images/", verbose_name="Do you want to upload a image", null=True, blank=True)
    company_name = models.CharField(max_length=200, verbose_name="Enter Company name", null=True, blank=True)
    post = models.CharField(max_length=200, verbose_name="Enter the post ", null=True, blank=True)

    linkedin_1_url = models.URLField(verbose_name="Enter company's Linkedin Profile", null=True, blank=True)
    is_working = models.BooleanField(verbose_name="Tick if currently working", blank=True)
    start_date1 = models.DateField(auto_now=True, verbose_name="Started project on", null=True, blank=True)
    end_date1 = models.DateField(auto_now=True, verbose_name="Project ended on", null=True, blank=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = 'My Internship'


class jobs(models.Model):
    is_show7 = models.BooleanField(verbose_name="Do you want to show it on portfolio")
    name10 = models.ForeignKey('Intro', on_delete=models.CASCADE)
    company_name1 = models.CharField(max_length=200, verbose_name="Enter Company name you worked as employee",
                                     null=True, blank=True)
    linkedin_2_url = models.URLField(verbose_name="Enter company's Linkedin Profile", null=True, blank=True)
    c_img2 = models.ImageField(upload_to="images/", null=True, blank=True)
    post1 = models.CharField(max_length=200, verbose_name="Enter the post ", null=True, blank=True)
    package = models.CharField(max_length=200, null=True, blank=True)
    is_working1 = models.BooleanField(verbose_name="Tick if currently working")
    start_date2 = models.DateField(auto_now=True, verbose_name="Started project on", null=True, blank=True)

    end_date2 = models.DateField(auto_now=True, verbose_name="Project ended on", null=True)

    def __str__(self):
        return str(self.post1)

    class Meta:
        verbose_name = 'My Job'
