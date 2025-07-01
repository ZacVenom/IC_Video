from manim import *

class SpringhillRansomwareVideo(Scene):
    def draw_icon(self, icon_type):
        if icon_type == "virus":
            arms = VGroup(*[
                Line(ORIGIN, 0.6 * RIGHT, color=RED).rotate(angle)
                for angle in [PI / 3, 2 * PI / 3, PI, 4 * PI / 3, 5 * PI / 3, 0]
            ])
            arms.shift(LEFT/3.5)
            core = Circle(radius=0.3, color=RED, fill_opacity=0.5)
            return VGroup(core, arms)

        elif icon_type == "hospital":
            base = RoundedRectangle(width=2, height=2.5, corner_radius=0.1, fill_color=BLUE_E, fill_opacity=0.8)
            cross_v = Rectangle(height=1, width=0.2, fill_color=WHITE, fill_opacity=1)
            cross_h = Rectangle(width=1, height=0.2, fill_color=WHITE, fill_opacity=1)
            cross = VGroup(cross_v, cross_h)
            return VGroup(base, cross)

        elif icon_type == "broken_chain":
            link1 = ArcBetweenPoints(LEFT * 0.6, ORIGIN, angle=PI / 2, color=GRAY)
            link2 = ArcBetweenPoints(ORIGIN, RIGHT * 0.6, angle=-PI / 2, color=GRAY)
            crack = Line(LEFT * 0.2 + DOWN * 0.2, RIGHT * 0.2 + UP * 0.2, color=RED)
            return VGroup(link1, link2, crack)

        elif icon_type == "alert":
            triangle = Triangle().scale(1.5).set_color(RED).set_fill(RED, 0.9)
            exclam = Text("!",font_size=90)
            return VGroup(triangle, exclam)

        elif icon_type == "leadership":
            left = Circle(radius=0.4, color=BLUE).shift(LEFT * 0.3)
            right = Circle(radius=0.4, color=GREEN).shift(RIGHT * 0.3)
            return VGroup(left, right)

        elif icon_type == "scale":
            beam = Line(LEFT * 2, RIGHT * 2, color=WHITE)
            stand = Line(ORIGIN, UP * 1.5, color=WHITE)
            pan_left = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5).shift(LEFT * 1.5 + DOWN)
            pan_right = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5).shift(RIGHT * 1.5 + DOWN * 0.5)
            return VGroup(beam, stand, pan_left, pan_right)

        elif icon_type == "globe":
            sphere = Circle(radius=0.8, color=BLUE_E, fill_opacity=0.5)
            lat_lines = VGroup(*[Circle(radius=0.8 * (1 - 0.2 * i), color=BLUE_B, stroke_width=1) for i in range(1, 4)])
            return VGroup(sphere, lat_lines)

        elif icon_type == "checklist":
            boxes = VGroup(
                Square(0.4, color=GREEN).shift(UP * 0.6),
                Square(0.4, color=GREEN),
                Square(0.4, color=GREEN).shift(DOWN * 0.6)
            )
            checks = VGroup(
                Line(UP*0.1 + LEFT * 0.1, ORIGIN, color=GREEN).shift(UP * 0.55),
                Line(ORIGIN, RIGHT * 0.15 + UP * 0.15, color=GREEN).shift(UP * 0.55),
                Line(UP*0.1 + LEFT * 0.1, ORIGIN, color=GREEN).shift(DOWN * 0.05),
                Line(ORIGIN, RIGHT * 0.15 + UP * 0.15, color=GREEN).shift(DOWN * 0.05),
                Line(UP*0.1 + LEFT * 0.1, ORIGIN, color=GREEN).shift(DOWN * 0.65),
                Line(ORIGIN, RIGHT * 0.15 + UP * 0.15, color=GREEN).shift(DOWN * 0.65),
            )
            return VGroup(boxes, checks)

        return Dot()
    
    
    def construct(self):
        def create_slider(self, topics, current_index):
            left = Text(topics[current_index - 1], font_size=24, fill_opacity=0.4) if current_index > 0 else Text(" ", font_size=24)
            center = Text(topics[current_index], font_size=30)
            right = Text(topics[current_index + 1], font_size=24, fill_opacity=0.4) if current_index < len(topics) - 1 else Text(" ", font_size=24)
            center.scale(0.4).center().to_edge(DOWN)
            left.scale(0.4).next_to(center,LEFT)
            right.scale(0.4).next_to(center,RIGHT)
            slider = VGroup(
                left,
                center,
                right
            )

            return slider

        def update_slider(self, slider, topics, current_index):
            new_slider = create_slider(self = self,topics = topics, current_index = current_index)
            if current_index < len(topics)-1:
                self.play(Transform(slider, new_slider), run_time=1)
            else:
                self.play(Transform(slider[:2],new_slider[:2]),FadeOut(slider[2]))
            return slider
        # Scene 1: Intro
        bg = Rectangle(width=14, height=8, fill_color=GRAY_E, fill_opacity=0.6,color=GRAY_E).set_z_index(-1)
        self.add(bg)
        topics = ["Springhill Medical Center",
                  "How Ransomware Works",
                  "Systemic Failures",
                  "Corporate Greed vs Human Life",
                  "Leadership in Crisis",
                  "Cultural Response to Crisis",
                  "Solutions and Policy"]
        title = Text("Ransomware at Springhill Medical Center", font_size=42, weight=BOLD)
        subtitle = Text("Lives Disrupted. Systems Broken. Leadership Missing.", font_size=28).next_to(title, DOWN)
        credit = Text("Peter  Šafranko",font_size = 20).next_to(subtitle,DOWN)
        self.play(Write(title, shift=UP))
        self.play(Write(subtitle, shift=UP))
        self.play(Write(credit))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(subtitle),FadeOut(credit))

        fade = Rectangle(width=14, height=8, fill_color=BLACK, fill_opacity=0.5,color = GRAY_E).set_z_index(-1)

        tragedy = Text(
            "A child died.\n\nDoctors were locked out of the system.\nNo access to medication or records.\nAccess to medical equipment restricted.",
            font_size=34, color=WHITE
        )
        self.play(FadeIn(tragedy))
        self.wait(1)
        self.play(tragedy.animate.set_color(RED),FadeIn(fade),run_time=2)
        self.wait(3)
        self.play(FadeOut(tragedy))
        self.wait(2)
        first_title = Text("Springhill Medical Center - 2019",font_size = 50,color=RED)
        self.play(FadeIn(first_title),run_time = 2)
        self.wait(6)
        self.play(FadeOut(fade))

        # Scene 2: The Springhill Case - 20 seconds
        title = Text("Springhill Medical Center - 2019", font_size=44).to_edge(UP)
        slider = create_slider(self = self,topics = topics,current_index = 0)
        self.play(FadeIn(slider))
        self.play(ReplacementTransform(first_title,title))
        self.wait()
        hospital = self.draw_icon("hospital").shift(LEFT * 4)
        broken_chain = self.draw_icon("broken_chain").next_to(hospital, RIGHT* 2)

        bullet_points = BulletedList(
            "Internal systems shut down",
            "No access to monitoring systems",
            "Doctors unaware of distress signals",
            "A baby died as a result",
            font_size=28
        ).next_to(broken_chain, RIGHT* 2)

        self.play(Write(hospital), Write(broken_chain))
        for i in range(4):
            self.play(Write(bullet_points[i]))
            self.wait()
        self.wait(11)
        self.play(FadeOut(title), FadeOut(hospital), FadeOut(broken_chain), FadeOut(bullet_points),run_time = 2)
         # Scene 3: How Ransomware Works 23 - 29
        slider = update_slider(self = self, slider = slider, topics = topics, current_index = 1)

        title = Text("How Ransomware Works", font_size=44).to_edge(UP)
        self.play(FadeIn(slider))
        self.play(Write(title))

        virus_icon = self.draw_icon("virus").shift(LEFT * 4)

        steps = VGroup(
            Text("1. Entry point: Phishing or exposed systems", font_size=28),
            Text("2. Encryption: Patient files are locked", font_size=28),
            Text("3. Ransom note: 'Pay or lose everything'", font_size=28),
            Text("4. Threat: Data deletion or exposure", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(virus_icon, RIGHT * 2)
        self.play(GrowFromCenter(virus_icon))
        for i in range(4):
            self.play(Write(steps[i]))
            self.wait()
        self.wait(11)
        self.play(steps.animate.shift(LEFT*2),virus_icon.animate.shift(LEFT*2))
        extra = Text("-> No guarantee",font_size=28).next_to(steps[2],RIGHT)
        self.play(Write(extra))
        self.wait(6)
        self.play(FadeOut(title), FadeOut(virus_icon), FadeOut(steps),FadeOut(extra),run_time = 2)
        # Scene 4: Systemic Failures - 18
        title = Text("Systemic Failures", font_size=44).to_edge(UP)
        slider = update_slider(self = self, slider = slider, topics = topics, current_index = 2)
        red_cross = self.draw_icon("alert").shift(LEFT * 4)

        failures = BulletedList(
            "No real-time monitoring fallback",
            "No backup protocols",
            "No transparent reporting to staff",
            "No cybersecurity investment",
            font_size=28
        ).next_to(red_cross, RIGHT* 2)

        self.play(Write(title), GrowFromCenter(red_cross))
        for i in range(4):
            self.play(Write(failures[i]))
            self.wait()
        self.wait(9)
        self.play(FadeOut(title), FadeOut(red_cross), FadeOut(failures),run_time = 2)
        # Scene 5: Corporate Greed - 18
        title = Text("Corporate Greed vs Human Life", font_size=44).to_edge(UP)
        update_slider(self = self, slider = slider, topics = topics, current_index = 3)
        scale = self.draw_icon("scale").shift(LEFT * 4)

        greed_points = BulletedList(
            "Hospitals store life-critical data",
            "Leadership holds life-or-death power",
            "Keeping systems secure is a moral duty",
            "Profit was prioritized over protection",
            font_size=28
        ).next_to(scale, RIGHT* 2)

        self.play(Write(title), Write(scale))
        for i in range(4):
            self.play(Write(greed_points[i]))
            self.wait()
        self.wait(9)
        self.play(FadeOut(title), FadeOut(scale), FadeOut(greed_points),run_time = 2)

        # Scene 6: Leadership Styles - 18
        slider = update_slider(self = self, slider = slider, topics = topics, current_index = 4)
        title = Text("Leadership in Crisis", font_size=44).to_edge(UP)
        yin_yang = self.draw_icon("leadership").shift(LEFT * 4)

        styles = BulletedList(
            "No shared decision-making in crisis",
            "Springhill kept staff in the dark",
            "Coercive leadership style",
            "No one felt responsible",
            font_size=28
        ).next_to(yin_yang, RIGHT* 2)

        self.play(Write(title), Write(yin_yang))
        for i in range(4):
            self.play(Write(styles[i]))
            self.wait()
        self.wait(9)
        self.play(FadeOut(title), FadeOut(yin_yang), FadeOut(styles),run_time = 2)
        # Scene 7: Culture in Crisis - 33
        slider = update_slider(self = self, slider = slider, topics = topics, current_index = 5)
        title = Text("Cultural Response to Crisis", font_size=44).to_edge(UP)
        globe = self.draw_icon("globe").shift(LEFT * 4)

        culture = BulletedList(
            "Hofstede: Uncertainty Avoidance Index",
            "Lewis Model: Multi-active vs linear-active",
            "High-context vs low-context communication",
            "Crisis protocols depend on culture",
            font_size=28
        ).next_to(globe, RIGHT* 2)

        self.play(Write(title), Write(globe))
        for i in range(4):
            self.play(Write(culture[i]))
            self.wait()
        self.wait(25)
        self.play(FadeOut(title), FadeOut(globe), FadeOut(culture),run_time = 2)

        # Scene 8: Solutions 18
        slider = update_slider(self = self, slider = slider, topics = topics, current_index = 6)
        title = Text("Solutions and Policy", font_size=44).to_edge(UP)
        check = self.draw_icon("checklist").shift(LEFT * 4)

        solutions = BulletedList(
            "Update and patch systems regularly",
            "No private hospitals for critical care",
            "Mandatory breach disclosure laws",
            "Education on old-school medical equipment and procedures",
            "Cybersecurity education for leadership",
            font_size=28
        ).next_to(check, RIGHT* 2)

        self.play(Write(title), Write(check))
        for i in range(5):
            self.play(Write(solutions[i]))
            self.wait()
        self.wait(7)
        self.play(FadeOut(slider))
        self.play(FadeOut(title), FadeOut(check), FadeOut(solutions),run_time = 2)
        
        # Final Message
        final = Text("Cybersecurity is Leadership in Action", font_size=36)
        self.play(Write(final))
        self.wait(3)
        self.play(FadeOut(final),run_time = 2)
        #Credits
        made_using = Text("Made using").shift(UP*2)
        banner = ManimBanner().next_to(made_using,DOWN)
        self.play(Write(made_using),run_time = 2)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner),Unwrite(made_using))
        self.wait(1)
        github = Text("The video code can be found on GitHub:\nhttps://github.com/ZacVenom/IC_Video")
        self.play(FadeIn(github))
        self.wait(5)
        self.play(FadeOut(github))
