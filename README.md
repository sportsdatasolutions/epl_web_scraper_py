## EPL Web Scraper ([Deepnote Edition](https://deepnote.com/publish/19f51d7b-ae79-4c51-906c-dee0138da144))

> [Official EPL Goals Stats](https://www.premierleague.com/stats/) Web Scraper [Built in Deepnote](https://deepnote.com/project/19f51d7b-ae79-4c51-906c-dee0138da144#%2Fepl_web_scraper.ipynb) (designed to run anywhere).

![EPLSiteScreen](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/EPLsitescreen.png)

### Story

The **[Official EPL Stats Website](https://www.premierleague.com/stats/)** is a great source of quality data in regards to Football, specifically the English Premier League. The **[Player Goals Table](https://www.premierleague.com/stats/top/players/goals?se=363)** specifically fetches data from the ***Pulse Live Football API*** (footballapi.pulselive.com). Use browser tools > network (refresh page) > XHR to see the ```goals?``` request. However, if you try and request that data yourself through the browser, e.g copy past the query to pulse live API, **your request will be denied!** 🙅‍♂️

So, we need to scrape the HTML. However, if we were to simply ***request*** the page html, we'd get the initial page load which defaults to the ***all-time goal scorers list*** (example of this in [```epl_web_scraper.ipynb```](./epl_web_scraper.ipynb)). We'd aslo have a problem scraping all the goal scorers because the table is **paginated**. So..we know the data in the table is **dynamically loaded**, and a **simple http request** of the html is **not enough**.

**All this means it's time to break out the headless browser, automate with watir, parse tables with pandas, sit back..and enjoy** 👻🤖🐼💅

### Getting Started

> You can either Fork this repo and Clone your Fork locally, or duplicate the project on Deepnote.

```markdown
## Deepnote

1a. Duplicate (e.g. clone) from the published Deepnote project: https://deepnote.com/publish/19f51d7b-ae79-4c51-906c-dee0138da144
1b. Or, try from the actual Deepnote project: https://deepnote.com/project/19f51d7b-ae79-4c51-906c-dee0138da144
1c. Alternatively, fork this repo then link your fork to a new Deepnote Project,
2c. Drag folders/files into deepnote root and delete empty epl_web_scraper_py folder,
3c. See [init.ipynb (in Environment Tab)](https://deepnote.com/project/19f51d7b-ae79-4c51-906c-dee0138da144#%2Finit.ipynb) for more info on how the environment is customised to support web scraping via headless browser. Make sure you copy over the Pipfile and Chrome Driver code cells to your projects init.ipynb file.
```

```markdown
## Fork & Clone

1. Fork this Repo
2. Clone your fork locally

$ git clone git@github.com:githubusername/epl_web_scraper.git && cd epl_web_scraper

3. Install Dependencies with Pipenv

$ pip install pipenv
$ pipenv install

4. Install Chrome Driver (See https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) e.g.

#### Linux (WSL TBC)
$ sudo apt-get update
$ sudo apt-get install chromium-driver -y

#### MacOS w/ Homebrew (See https://brew.sh/)

$ brew tap homebrew/cask && brew cask install chromedriver
```

#### ```Dependencies```

> See [Pipfile](./Pipfile).

**Note**: If installing ***locally***, make sure you add **```jupyter```** to the **Pipfile** or use **```pipenv```** to install if you want to use the notebook version e.g.

```bash
$ pipenv install jupyter
```

#### ```Running```

> You have the option to either run the script (```.py```) version of the scraper or the notebook (```.ipynb```) version of the web scraper.

```markdown
## Deepnote

#### epl_goals_scraper.py

Open a Terminal within Deepnote Project.

$ python epl_goals_scraper.py

#### epl_goals_scraper.ipynb

Open and click Run notebook.
```

```markdown
## Locally

#### epl_goals_scraper.py

$ pipenv run python epl_goals_scraper.py

#### epl_goals_scraper.ipynb

$ pipenv run jupyter notebook .

Now open jupyter console and navigate to epl_goals_scraper.ipynb to run
```

#### ```Contributing```

> See [contributing.md](./contributing.md).
