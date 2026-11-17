# -*- coding: utf-8 -*-
"""Editorial content for Beautiful.Life. Add new articles to ARTICLES and re-run build.py."""

PILLARS = [
    # slug, name, emoji, tagline, intro
    ("mind", "Mind", "🧠", "Calm, clarity and emotional strength",
     "Your inner life sets the tone for everything else. Here you'll find research-backed practices for managing stress, building resilience and training attention — the quiet skills behind a beautiful life."),
    ("body", "Body", "🌿", "Sleep, movement and nourishment",
     "Energy is the currency of a good day. These guides focus on the fundamentals with the strongest evidence: sleep, daily movement, simple nutrition and recovery."),
    ("money", "Money", "💰", "Calm finances and freedom",
     "Money can't buy happiness, but financial stress reliably takes it away. Learn to build a buffer, spend on what matters and design a path to more freedom and choice."),
    ("love", "Love", "💞", "Friendship, family and connection",
     "Decades of research point to one conclusion: the quality of our relationships predicts the quality of our lives. Practical guides to deeper friendships, better conversations and lasting love."),
    ("home", "Home", "🏡", "Spaces that restore you",
     "Your surroundings shape your mood more than you think. Ideas for calmer, lighter, more intentional homes — at any budget."),
    ("purpose", "Purpose", "🌅", "Meaning, values and direction",
     "A beautiful life has a 'why'. Tools and reflections to clarify your values, find meaningful work and live with direction."),
    ("adventure", "Adventure", "🧭", "Travel, novelty and awe",
     "Novelty and awe are fuel for a full life. From weekend micro-adventures to bucket-list travel, we help you collect experiences, not clutter."),
    ("growth", "Growth", "📚", "Habits, learning and self-mastery",
     "Small habits compound into big lives. Systems for learning, focus and personal growth that fit real schedules."),
]

ARTICLES = [
{
"slug": "science-of-a-good-life",
"title": "The Science of a Good Life: What Decades of Research Agree On",
"desc": "Long-running studies of human wellbeing keep pointing to the same few ingredients. Here's what they are and how to put them to work this week.",
"cat": "love", "emoji": "🔬", "mins": 8, "date": "2026-11-16",
"body": """
<p>Ask a hundred people what makes a life beautiful and you'll hear a hundred answers: travel, family, freedom, faith, success, peace. Ask researchers who have followed thousands of people for decades and the list gets surprisingly short. This guide distils what the long-term evidence on wellbeing agrees on, and turns it into actions you can start today.</p>
<h2 id="relationships">1. Relationships are the strongest predictor</h2>
<p>The Harvard Study of Adult Development began in 1938 and has followed its original participants — and later their children — across their entire lives. Its most cited conclusion is simple: people with warm, dependable relationships were happier and healthier in later life than people who were more isolated, regardless of wealth or fame. The quality of relationships in midlife predicted wellbeing in old age better than cholesterol levels did.</p>
<p>The practical lesson is not "be more social" in the abstract. It's to treat relationships like any other important investment: schedule them, maintain them and repair them when they break.</p>
<div class="callout"><b>Try this week:</b> list the five people you most want in your life in ten years. Next to each name, write the last time you had a real conversation. Book the most overdue one.</div>
<h2 id="meaning">2. Meaning beats pleasure over the long run</h2>
<p>Psychologists distinguish between <em>hedonic</em> wellbeing (feeling good) and <em>eudaimonic</em> wellbeing (living in line with your values and potential). Both matter, but people who report a strong sense of purpose tend to cope better with setbacks and stay engaged as they age. Pleasure fades quickly as we adapt to it; meaning tends to accumulate.</p>
<p>Meaning rarely arrives as a single grand mission. More often it comes from contribution — caring for someone, creating something, teaching, building, serving a community.</p>
<h2 id="health">3. The basics are not optional</h2>
<p>Sleep, movement and nutrition sound boring next to purpose and love, but they set the ceiling for everything else. Chronic sleep loss is linked with lower mood, worse decision-making and poorer emotional regulation. Regular physical activity is one of the most consistently supported tools for both physical and mental health. You can't journal your way out of exhaustion.</p>
<h2 id="money">4. Money matters — up to a point, and in specific ways</h2>
<p>Research on income and happiness is more nuanced than the old "money doesn't buy happiness" slogan. Higher income is generally associated with higher life satisfaction, but how you spend matters a great deal. Studies by social psychologists have found that spending on experiences, on buying back time and on other people tends to produce more lasting satisfaction than spending on more possessions. Financial security — having a buffer — reduces a specific and corrosive kind of stress.</p>
<h2 id="attention">5. Where your attention goes, your life goes</h2>
<p>Experience-sampling studies, which ping people at random moments to ask what they're doing and how they feel, have found that our minds wander a large share of the time and that mind-wandering is often associated with lower mood. Practices that train attention — mindfulness, savouring, deliberate gratitude — are less about relaxation and more about choosing what you notice.</p>
<h2 id="plan">A simple weekly plan</h2>
<ol>
<li><b>Connect:</b> one unhurried conversation with someone who matters.</li>
<li><b>Contribute:</b> one act that helps someone else, however small.</li>
<li><b>Recover:</b> protect seven or more hours of sleep on at least five nights.</li>
<li><b>Move:</b> 150 minutes of moderate activity, spread across the week.</li>
<li><b>Notice:</b> each evening, write down three things that went well.</li>
</ol>
<blockquote>A beautiful life is not a destination you arrive at. It's a set of small, repeatable choices.</blockquote>
<p>If you want a clear picture of where to start, our free <a href="../tools/wheel-of-life.html">Wheel of Life assessment</a> shows which of the eight life areas will give you the biggest return on your effort.</p>
"""},
{
"slug": "wheel-of-life-guide",
"title": "The Wheel of Life: How to Audit Your Whole Life in 15 Minutes",
"desc": "A step-by-step guide to the classic coaching exercise that reveals where your life is out of balance — and what to do about it.",
"cat": "growth", "emoji": "🎡", "mins": 6, "date": "2026-11-14",
"body": """
<p>Most of us only notice that something is off when it becomes a crisis: burnout, a health scare, a relationship at breaking point. The Wheel of Life is a simple coaching exercise that catches imbalance early. It takes about fifteen minutes and gives you a single picture of your whole life.</p>
<h2>How the exercise works</h2>
<p>You divide life into a handful of areas — we use eight: Mind, Body, Money, Love, Home, Purpose, Adventure and Growth. You rate your satisfaction with each from 1 to 10, then plot the scores on a circle. The result looks like a wheel, and the question is obvious: how smoothly would this wheel roll?</p>
<h2>Step 1: Rate honestly, not ideally</h2>
<p>Score how things are today, not how they were last year or how you hope they'll be. A useful rule: a 10 means you would not change anything; a 5 means it's fine but you often think about it; a 2 means it's actively hurting other areas of your life.</p>
<h2>Step 2: Look for the shape, not the average</h2>
<p>An average of 6 can hide very different lives. Someone with 9s in Money and Purpose and 2s in Body and Love has a very different problem from someone with steady 6s everywhere. Large gaps between your highest and lowest areas usually mean the strong areas are being funded by the weak ones — long hours at work paid for with sleep and relationships, for example.</p>
<h2>Step 3: Choose one area — and only one</h2>
<p>It's tempting to fix everything. Don't. Choose the area where a two-point improvement would most change how you feel day to day. Often that's the lowest score, but not always: sometimes a modest improvement in Body (better sleep) lifts Mind, Love and Growth at the same time.</p>
<div class="callout"><b>The ripple test:</b> for each area, ask "If this went up by two points, how many other areas would improve too?" Choose the area with the most ripples.</div>
<h2>Step 4: Define a 30-day experiment</h2>
<p>Turn the chosen area into one specific, measurable behaviour you'll try for 30 days. "Improve health" is a wish. "Lights out by 11pm on weeknights" is an experiment. Track it with our free <a href="../tools/habit-tracker.html">habit tracker</a>.</p>
<h2>Step 5: Re-score every month</h2>
<p>Repeat the wheel monthly. You'll see whether your experiment worked and spot new imbalances before they turn into problems. Over a year, those twelve snapshots become a remarkably honest diary of your life.</p>
<h2>Common mistakes</h2>
<ul>
<li><b>Comparing your wheel with someone else's.</b> The point is your own balance, not a competition.</li>
<li><b>Treating 10 as the goal everywhere.</b> A life of all 10s doesn't exist. Aim for no area below 5 and steady movement upward.</li>
<li><b>Skipping the action step.</b> Insight without an experiment changes nothing.</li>
</ul>
<p>Ready? <a href="../tools/wheel-of-life.html">Open the interactive Wheel of Life</a>. It saves your scores privately in your browser so you can compare month to month.</p>
"""},
{
"slug": "morning-routine-that-sticks",
"title": "Morning Routines That Actually Stick (Without a 5am Alarm)",
"desc": "Forget the 27-step celebrity routine. Here's a flexible framework for mornings that give you energy instead of draining it.",
"cat": "body", "emoji": "🌄", "mins": 7, "date": "2026-11-12",
"body": """
<p>Online, the perfect morning routine involves a 5am alarm, an ice bath, an hour of journaling and a green smoothie. In real life, most people have children, commutes, night shifts or simply a body clock that doesn't cooperate. A routine you can't sustain does more harm than good because every failure chips away at your confidence.</p>
<p>Here's a better approach: a small set of building blocks you can arrange around your actual life.</p>
<h2>The four building blocks</h2>
<h3>1. Light</h3>
<p>Getting bright light — ideally daylight — soon after waking helps anchor your body clock, which supports alertness during the day and sleepiness at night. Open the curtains, step outside for a few minutes or have breakfast by a window.</p>
<h3>2. Hydrate</h3>
<p>A glass of water before coffee is the simplest habit on this list and a natural "anchor" that the rest of your routine can attach to.</p>
<h3>3. Move</h3>
<p>Not a workout, necessarily. Five minutes of stretching, a short walk or a few bodyweight exercises raise your energy and mood. If you exercise later in the day, keep the morning version tiny.</p>
<h3>4. Direct</h3>
<p>Spend two minutes deciding what matters today. Write down the one thing that would make today a success. This is the step that turns a pleasant morning into a productive day.</p>
<h2>Make it fit: three versions</h2>
<div class="grid g3">
<div class="card"><h3>10 minutes</h3><p>Water, open the curtains, 3 minutes of stretching, write your one thing.</p></div>
<div class="card"><h3>30 minutes</h3><p>Water, a 15-minute outdoor walk, a calm breakfast without screens, plan the day.</p></div>
<div class="card"><h3>60 minutes</h3><p>Water, exercise, shower, 10 minutes of reading or journaling, plan the day.</p></div>
</div>
<h2>Why routines fail — and how to fix it</h2>
<ul>
<li><b>Too big too soon:</b> start with the 10-minute version for two weeks before adding anything.</li>
<li><b>Relying on willpower:</b> prepare the night before. Put water by the bed and your walking shoes by the door.</li>
<li><b>The phone trap:</b> checking messages first hands your morning to other people's priorities. Keep your phone out of reach until your routine is done.</li>
<li><b>Ignoring evenings:</b> a good morning starts the night before. If you're short on sleep, no routine will feel good. Our <a href="../tools/sleep-calculator.html">sleep calculator</a> can help you time your bedtime.</li>
</ul>
<blockquote>Win the first hour gently, and the rest of the day becomes easier to win.</blockquote>
<h2>Shift workers and parents</h2>
<p>"Morning" simply means the first hour after you wake, whenever that is. Night-shift workers can apply the same blocks after their main sleep period. Parents can stack the routine onto the children's routine: water and light while making breakfast, a walk on the school run, planning on the commute.</p>
"""},
{
"slug": "sleep-better-guide",
"title": "Sleep: The Most Underrated Beauty Treatment There Is",
"desc": "Good sleep improves mood, focus, skin and health. A practical, evidence-informed guide to sleeping better starting tonight.",
"cat": "body", "emoji": "🌙", "mins": 8, "date": "2026-11-10",
"body": """
<p>If someone sold a product that improved mood, sharpened focus, supported immunity and helped you look more rested, it would be the best-selling item on earth. It already exists, it's free, and most of us don't get enough of it. Health authorities generally recommend that adults get at least seven hours of sleep a night, yet a large share of adults regularly fall short.</p>
<h2>Why sleep matters so much</h2>
<p>During sleep the body repairs tissue, consolidates memories and regulates hormones involved in appetite and stress. After short sleep, people tend to be more irritable, find it harder to concentrate and make riskier choices. Over the long term, chronic short sleep is associated with a range of health problems.</p>
<h2>The seven habits with the biggest payoff</h2>
<ol>
<li><b>Keep a consistent wake time</b> — even on weekends. Consistency anchors your body clock more than bedtime does.</li>
<li><b>Get morning daylight</b> to strengthen your natural day–night rhythm.</li>
<li><b>Cut caffeine after early afternoon.</b> Caffeine can stay in your system for many hours.</li>
<li><b>Make your room cool, dark and quiet.</b> Blackout curtains and an eye mask are among the cheapest upgrades.</li>
<li><b>Create a wind-down buffer</b> of 30–60 minutes: dim lights, no work email, something calming.</li>
<li><b>Go easy on alcohol before bed.</b> It may help you fall asleep, but it tends to fragment sleep later in the night.</li>
<li><b>Get up if you can't sleep.</b> After about 20 minutes awake, go to another room and do something calm until you feel sleepy.</li>
</ol>
<div class="callout"><b>Sleep cycles:</b> sleep moves through cycles of roughly 90 minutes. Waking at the end of a cycle often feels easier than waking in the middle of deep sleep. Use our <a href="../tools/sleep-calculator.html">sleep calculator</a> to plan around them.</div>
<h2>Shift work and irregular schedules</h2>
<p>If you work nights, protect your main sleep block like an appointment: blackout curtains, earplugs or white noise, phone on do-not-disturb, and a short wind-down routine even after a morning finish. Wearing sunglasses on the drive home after a night shift can help your body prepare for sleep.</p>
<h2>When to get help</h2>
<p>Loud snoring with gasping, persistent difficulty falling or staying asleep for months, or extreme daytime sleepiness are reasons to speak with a doctor. Sleep disorders are common and treatable. <em>This article is for general information and is not medical advice.</em></p>
"""},
{
"slug": "money-and-happiness",
"title": "Money and Happiness: How to Spend for a More Beautiful Life",
"desc": "Research suggests that how you spend matters as much as how much you earn. Five spending principles that buy more joy per dollar.",
"cat": "money", "emoji": "💸", "mins": 7, "date": "2026-11-08",
"body": """
<p>"Money can't buy happiness" is half true. Research shows that financial security reduces stress, and that higher income is generally linked with higher life satisfaction. But research also shows that two people with the same income can get very different amounts of wellbeing from it, depending on how they spend. Here are five principles that help each dollar do more.</p>
<h2>1. Buy experiences more than things</h2>
<p>Studies have repeatedly found that experiential purchases — trips, concerts, classes, meals with friends — tend to bring more lasting satisfaction than material ones. Experiences become part of your story, are often shared with others and are harder to compare unfavourably with what other people have.</p>
<h2>2. Buy back your time</h2>
<p>Research by social psychologists has found that people who spend money to save time — outsourcing a disliked chore, paying for a shorter commute — tend to report greater life satisfaction. If an hour of your time is worth more to you than the cost of a cleaner or a grocery delivery, the trade may be a good one.</p>
<h2>3. Spend on other people</h2>
<p>Experiments on "prosocial spending" have found that spending money on others or giving to good causes tends to boost the giver's happiness more than spending the same amount on themselves. The amount doesn't need to be large.</p>
<h2>4. Delay consumption — and enjoy the anticipation</h2>
<p>Looking forward to something is a pleasure in itself. Booking a holiday months in advance gives you weeks of anticipation. Paying now and enjoying later also tends to make the eventual experience feel "free".</p>
<h2>5. Build a buffer before upgrading your lifestyle</h2>
<p>Few purchases improve day-to-day wellbeing as much as knowing an unexpected bill won't become a crisis. An emergency fund is one of the least glamorous and most effective "happiness purchases" you can make. See our guide to <a href="calm-money-emergency-fund.html">building an emergency fund</a>.</p>
<div class="callout"><b>Joy-per-dollar audit:</b> look at your last month's spending. Mark each item ★ (brought real joy or calm), ○ (neutral) or ✗ (regret). Cut the ✗s and redirect the money to more ★s.</div>
<h2>What about big purchases?</h2>
<p>People adapt quickly to larger homes, nicer cars and new gadgets — a process psychologists call hedonic adaptation. That doesn't mean never upgrade; it means expect the thrill to fade and make sure the purchase also solves a real, recurring problem (a shorter commute, more space for a growing family).</p>
<p>Curious how close you are to financial independence? Try our <a href="../tools/freedom-calculator.html">Financial Freedom Calculator</a>. <em>This article is general information, not personal financial advice.</em></p>
"""},
{
"slug": "calm-money-emergency-fund",
"title": "The Calm-Money Method: Build an Emergency Fund on Any Income",
"desc": "An emergency fund is the foundation of financial peace of mind. Here is a step-by-step plan that works even on a tight budget.",
"cat": "money", "emoji": "🛟", "mins": 7, "date": "2026-11-06",
"body": """
<p>An emergency fund is money set aside for the unexpected: a job loss, a car repair, an urgent trip home. It isn't exciting, but it is the single financial habit most likely to turn a crisis into an inconvenience. Here's how to build one, step by step.</p>
<h2>How much do you need?</h2>
<p>A common guideline is three to six months of essential expenses — rent or mortgage, utilities, food, insurance, transport and minimum debt payments. Aim for the higher end if your income is irregular, you're self-employed or you support others. Start smaller, though: even one month of expenses provides real protection.</p>
<h2>The four-stage plan</h2>
<ol>
<li><b>Starter buffer:</b> save a small, fixed amount — enough to cover a typical surprise bill. This stops small emergencies going onto high-interest credit.</li>
<li><b>One month:</b> build to one month of essential expenses.</li>
<li><b>Three months:</b> the point where most people say they feel "safe".</li>
<li><b>Six months:</b> full peace of mind, especially for variable incomes.</li>
</ol>
<h2>Where to keep it</h2>
<p>The fund should be safe, separate and accessible. A high-interest savings account at a regulated institution, separate from your everyday account, is a common choice. Separation matters: if the money sits next to your spending money, it tends to get spent.</p>
<h2>How to find the money</h2>
<ul>
<li><b>Automate it:</b> set up a transfer on payday so saving happens before spending.</li>
<li><b>Save windfalls:</b> tax refunds, bonuses and gifts can jump-start the fund.</li>
<li><b>Cancel one subscription</b> and redirect the payment.</li>
<li><b>Round up:</b> many banks offer features that round purchases up and save the difference.</li>
<li><b>Sell what you don't use:</b> clearing clutter can fund your first stage.</li>
</ul>
<div class="callout"><b>Define "emergency" in advance.</b> Write down what counts — job loss, medical costs, essential repairs — and what doesn't (sales, holidays). Deciding now protects the fund from future temptation.</div>
<h2>After you use it</h2>
<p>Using the fund isn't failure; it's the fund doing its job. Pause other goals briefly and rebuild it before resuming.</p>
<p><em>General information only. For advice tailored to your situation, speak with a qualified financial professional — you can <a href="../get-matched.html">request a match here</a>.</em></p>
"""},
{
"slug": "gratitude-journaling",
"title": "Gratitude Journaling: A Five-Minute Habit With Real Effects",
"desc": "Writing down what went well is one of the most studied positive-psychology practices. How to do it so it doesn't feel forced.",
"cat": "mind", "emoji": "📓", "mins": 6, "date": "2026-11-04",
"body": """
<p>Gratitude practices are among the most studied interventions in positive psychology. In a well-known set of experiments, psychologists Robert Emmons and Michael McCullough asked participants to keep weekly lists of things they were grateful for; compared with groups who listed hassles or neutral events, the gratitude group tended to report feeling better about their lives. Later research has explored many variations, with generally modest but meaningful benefits.</p>
<p>The catch: done mechanically, gratitude journaling can start to feel like a chore. Here's how to keep it fresh.</p>
<h2>The basic method</h2>
<p>Once a day, or a few times a week, write down three specific things you're grateful for. Some research suggests that writing a few times a week can feel fresher than writing every day, so experiment with frequency.</p>
<h2>Five rules that make it work</h2>
<ol>
<li><b>Be specific.</b> "My family" is vague. "My sister texted to check how my interview went" is vivid.</li>
<li><b>Focus on people</b> more than things. Gratitude for people strengthens relationships.</li>
<li><b>Include the "why".</b> Asking why something happened links it to your choices and to other people's kindness.</li>
<li><b>Notice the surprising.</b> Unexpected good things carry more emotional weight than the routine.</li>
<li><b>Vary the prompts</b> to avoid repeating the same three items forever.</li>
</ol>
<h2>Prompts for when you're stuck</h2>
<ul>
<li>What made today a little easier than it could have been?</li>
<li>Which person would I miss if they disappeared from my life?</li>
<li>What did my body allow me to do today?</li>
<li>What challenge from the past am I now grateful for?</li>
<li>What did I see, hear or taste today that was beautiful?</li>
</ul>
<div class="callout"><b>Level up:</b> once a month, write a short gratitude letter to someone who has helped you, and if you can, read it to them. Many people find this one of the most moving exercises in positive psychology.</div>
<p>Start now with our private <a href="../tools/gratitude-journal.html">online gratitude journal</a>. Entries are stored only in your browser, and you can export them at any time.</p>
"""},
{
"slug": "calm-home-design",
"title": "Designing a Home That Calms You: 12 Ideas for Any Budget",
"desc": "Light, order, nature and personal meaning: simple ways to make your home feel like a place of rest rather than another to-do list.",
"cat": "home", "emoji": "🛋️", "mins": 7, "date": "2026-11-02",
"body": """
<p>Your home is the backdrop to most of your life. When it's cluttered, dark or chaotic, it quietly adds stress; when it's calm and personal, it helps you recover. You don't need a renovation to make a difference. Here are twelve ideas, from free to moderate cost.</p>
<h2>Free</h2>
<ol>
<li><b>Clear one surface completely.</b> A single clear table or counter makes a whole room feel calmer.</li>
<li><b>Create a "landing zone"</b> by the door for keys, bags and mail, so clutter has a home.</li>
<li><b>Maximise daylight:</b> clean the windows, open blinds fully and move furniture that blocks light.</li>
<li><b>Edit your decor.</b> Store half your ornaments and rotate them seasonally — they'll feel new again.</li>
<li><b>Make the bed every morning.</b> It takes two minutes and anchors the day.</li>
<li><b>Do a 10-minute evening reset</b> so you wake up to order rather than yesterday's mess.</li>
</ol>
<h2>Low cost</h2>
<ol start="7">
<li><b>Add plants.</b> Easy-care options include pothos and snake plants. Living things make spaces feel alive.</li>
<li><b>Switch to warm lighting</b> in the evening. Lamps at different heights feel more relaxing than a single bright ceiling light.</li>
<li><b>Use baskets and boxes</b> to hide visual noise on open shelves.</li>
<li><b>Display meaningful photos</b> — of people and places you love — rather than generic art.</li>
</ol>
<h2>Worth investing in</h2>
<ol start="11">
<li><b>A great mattress and blackout curtains.</b> You spend a third of your life in bed.</li>
<li><b>A dedicated calm corner:</b> a comfortable chair, a lamp and a small table for reading, tea or reflection.</li>
</ol>
<div class="callout"><b>The one-in, one-out rule:</b> each time something new comes into your home, something similar leaves. It's the easiest way to keep clutter from creeping back.</div>
<h2>Decluttering without overwhelm</h2>
<p>Tackle one small category at a time — a drawer, a shelf, your shoes — rather than a whole room. Sort into keep, donate, recycle and sell. Donating items you no longer use also turns clutter into contribution.</p>
"""},
{
"slug": "finding-your-purpose",
"title": "Finding Your Purpose: A Practical Framework (No Epiphany Required)",
"desc": "Purpose is usually built, not found. A four-question framework to discover meaningful direction in work and life.",
"cat": "purpose", "emoji": "🌅", "mins": 8, "date": "2026-10-30",
"body": """
<p>Many people wait for purpose to arrive like a lightning bolt. For most of us it doesn't work that way. Purpose is usually built gradually, through experiments, reflection and commitment. Here's a practical framework to start building yours.</p>
<h2>The four questions</h2>
<p>Inspired by the Japanese concept often described as <em>ikigai</em> — loosely, "a reason for being" — this framework looks for overlap between four areas:</p>
<div class="grid g2">
<div class="card"><h3>What do I love?</h3><p>Activities that absorb you so completely that you lose track of time.</p></div>
<div class="card"><h3>What am I good at?</h3><p>Skills others come to you for, or that you develop faster than most.</p></div>
<div class="card"><h3>What does the world need?</h3><p>Problems you notice and care about, from your street to the planet.</p></div>
<div class="card"><h3>What can I be valued for?</h3><p>Ways your contribution can be rewarded — financially or otherwise.</p></div>
</div>
<h2>Step 1: Collect evidence, not answers</h2>
<p>For two weeks, note moments when you feel energised and moments when you feel drained. Patterns appear quickly. Energy is information.</p>
<h2>Step 2: Clarify your values</h2>
<p>Choose your top five values from a list such as: freedom, family, creativity, security, adventure, service, learning, faith, health, excellence, community, beauty. Then rank them. Your purpose will feel right only if it honours your top values.</p>
<h2>Step 3: Run small experiments</h2>
<p>Instead of quitting your job to "find yourself", test ideas cheaply: volunteer for a weekend, take a short course, start a side project, interview someone who does work you admire. Each experiment either moves you closer or crosses an option off the list. Both are progress.</p>
<h2>Step 4: Write a working purpose statement</h2>
<p>Try this template: <em>"I use my [strengths] to [action] for [people or cause] so that [outcome]."</em> Example: "I use my patience and organisation to help older adults feel safe and dignified." Treat it as a draft you'll revise every year.</p>
<blockquote>Purpose is not a job title. It's the thread that connects what you do to why it matters.</blockquote>
<h2>Purpose outside of work</h2>
<p>Not everyone finds purpose in paid work, and that's fine. Raising children, caring for a parent, creating art, building community or practising faith are deep sources of meaning. A job can fund your purpose without being your purpose.</p>
<p>Want guided support? A qualified coach can speed up the process. <a href="../get-matched.html">Get matched with a life coach</a> for free.</p>
"""},
{
"slug": "breathing-techniques",
"title": "Three Breathing Techniques to Calm Your Mind in Under Five Minutes",
"desc": "Box breathing, 4-7-8 and coherent breathing: what they are, how to do them and when to use each.",
"cat": "mind", "emoji": "🌬️", "mins": 5, "date": "2026-10-28",
"body": """
<p>Your breath is the only part of your nervous system you can control directly and instantly. Slowing your breathing — especially lengthening the exhale — is widely used to shift the body toward a calmer state. These three techniques take less than five minutes and can be done anywhere.</p>
<h2>1. Box breathing (4-4-4-4)</h2>
<p>Breathe in for 4 counts, hold for 4, breathe out for 4, hold for 4. Repeat for four to six rounds. The even rhythm makes it easy to remember and gives an anxious mind something to focus on.</p>
<p><b>Best for:</b> before a presentation, a difficult conversation or any moment you need composure.</p>
<h2>2. 4-7-8 breathing</h2>
<p>Breathe in quietly through your nose for 4 counts, hold for 7, then exhale slowly through your mouth for 8. Repeat up to four times. The long exhale makes this a popular choice at bedtime.</p>
<p><b>Best for:</b> winding down before sleep or after a stressful day.</p>
<h2>3. Coherent breathing (5-5)</h2>
<p>Breathe in for about 5 seconds and out for about 5 seconds, smoothly and without holds — roughly six breaths per minute. Continue for five minutes or longer.</p>
<p><b>Best for:</b> a daily practice to build calm over time.</p>
<div class="callout"><b>Tips:</b> breathe through your nose where possible, let your belly rather than your shoulders rise, and never force the breath. If you feel light-headed, return to normal breathing.</div>
<h2>Practise with a guide</h2>
<p>Our free <a href="../tools/breathing-coach.html">breathing coach</a> animates each technique so you can simply follow along.</p>
<p><em>If you have a respiratory or heart condition, or you're pregnant, check with your healthcare provider before practising breath-holds. This content is for general wellbeing information only.</em></p>
"""},
{
"slug": "making-friends-as-an-adult",
"title": "How to Make Close Friends as an Adult (It Takes Time — Here's How Much)",
"desc": "Friendship after school and university doesn't happen by accident. A realistic, research-informed plan for building close friendships.",
"cat": "love", "emoji": "🤝", "mins": 7, "date": "2026-10-26",
"body": """
<p>As children, friendships form almost automatically: you see the same people every day, with time to spare and few responsibilities. As adults, those conditions disappear. If you've found it hard to make close friends after school, university or a move, you're not alone — and it isn't a personal failing. It's a structural problem with a practical solution.</p>
<h2>Friendship runs on time</h2>
<p>A study by communication researcher Jeffrey Hall estimated that it takes roughly 50 hours of time together to go from acquaintance to casual friend, around 90 hours to become a friend, and more than 200 hours to become a close friend. The exact numbers vary, but the principle is clear: closeness is built through repeated time together.</p>
<h2>The three conditions for friendship</h2>
<ol>
<li><b>Proximity:</b> seeing the same people regularly.</li>
<li><b>Repeated, unplanned interaction:</b> chances to bump into each other without organising it.</li>
<li><b>A setting that encourages openness:</b> where people can relax and share.</li>
</ol>
<p>The fastest route to adult friendship is to recreate these conditions deliberately.</p>
<h2>Six practical moves</h2>
<ul>
<li><b>Join something recurring:</b> a weekly class, a running club, a choir, a volunteer shift. Recurrence beats one-off events.</li>
<li><b>Be the initiator.</b> Most people are waiting to be invited. Suggest coffee or a walk.</li>
<li><b>Follow up within a week</b> after meeting someone you click with.</li>
<li><b>Turn activities into rituals</b> — a monthly dinner or a Sunday walk — so you don't renegotiate every time.</li>
<li><b>Share a little more</b> each time. Closeness grows through gradual, mutual openness.</li>
<li><b>Revive dormant ties.</b> Old friends and former colleagues are often the fastest path to closeness.</li>
</ul>
<div class="callout"><b>This week:</b> message one person you've lost touch with. Something simple works: "Saw this and thought of you — how have you been?"</div>
<h2>Maintaining friendships</h2>
<p>Friendships fade mostly through neglect, not conflict. A light rhythm of check-ins — a message every couple of weeks, a meetup every month or two — keeps them alive. Put birthdays and important dates in your calendar.</p>
"""},
{
"slug": "micro-adventures",
"title": "Micro-Adventures: How to Add Wonder to Ordinary Weeks",
"desc": "You don't need a passport or a big budget to feel alive. 25 micro-adventure ideas you can do this weekend.",
"cat": "adventure", "emoji": "🏕️", "mins": 6, "date": "2026-10-24",
"body": """
<p>Big trips are wonderful but rare. Micro-adventures — short, local, low-cost experiences that break routine — can bring novelty and awe into ordinary weeks. Researchers who study awe describe it as the feeling of encountering something vast that changes how you see the world, and it can be found far closer to home than you might think.</p>
<h2>Why novelty matters</h2>
<p>Routine makes time blur: weeks that look the same are hard to tell apart in memory. New experiences create distinct memories, which can make life feel richer and fuller. Novelty, shared with others, also strengthens relationships.</p>
<h2>25 micro-adventure ideas</h2>
<h3>Outdoors</h3>
<ul>
<li>Watch the sunrise from the highest point in your town.</li>
<li>Sleep under the stars in the garden or at a nearby campsite.</li>
<li>Walk a local trail you've never tried.</li>
<li>Go wild swimming at a safe, supervised spot.</li>
<li>Follow a river or stream as far as you can in two hours.</li>
<li>Go stargazing away from city lights.</li>
<li>Try foraging with a qualified guide.</li>
</ul>
<h3>In town</h3>
<ul>
<li>Take a bus to the end of the line and explore.</li>
<li>Eat a cuisine you've never tried.</li>
<li>Visit a museum and focus on just one room.</li>
<li>Be a tourist in your own city for a day.</li>
<li>Attend a free lecture or community event.</li>
<li>Find the oldest building in your area and learn its story.</li>
</ul>
<h3>Creative and social</h3>
<ul>
<li>Take a one-off class: pottery, dance, climbing.</li>
<li>Host a themed dinner with friends.</li>
<li>Start a "first Friday" tradition of doing something new each month.</li>
<li>Photograph your neighbourhood from a new perspective.</li>
<li>Learn to cook a dish from your family's heritage.</li>
<li>Volunteer somewhere unfamiliar.</li>
<li>Write a letter to your future self and seal it for a year.</li>
<li>Try an open-mic night — watching or performing.</li>
<li>Spend a phone-free day.</li>
<li>Plan a picnic in an unusual location.</li>
<li>Join a local walking tour.</li>
<li>Take a different route to work every day for a week.</li>
</ul>
<div class="callout"><b>Share your adventures:</b> our monthly <a href="../contests.html">Beautiful Moments contest</a> rewards the best stories and photos.</div>
"""},
]
