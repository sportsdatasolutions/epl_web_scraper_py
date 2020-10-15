## EPL Web Scraper [<img height="31" align="right" src="https://beta.deepnote.com/buttons/launch-in-deepnote.svg">](https://deepnote.com/project/19f51d7b-ae79-4c51-906c-dee0138da144)

![EPLSiteScreen](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/EPLsitescreen.png)

### Story

The **[Official EPL Stats Website](https://www.premierleague.com/stats/)** is a great source of quality data in regards to Football, specifically the English Premier League. The **[Player Goals Table](https://www.premierleague.com/stats/top/players/goals?se=363)** specifically fetches data from the ***Pulse Live Football API*** (footballapi.pulselive.com). Use browser tools > network (refresh page) > XHR to see the ```goals?``` request. However, if you try and request that data yourself through the browser, e.g copy paste the query to pulse live API, **your request will be denied!** 🙅‍♂️

So, we need to scrape the **HTML**. However, if we were to simply ***request*** the page's html (via http get request), we'd get the initial page load which defaults to the ***all-time goal scorers list*** (example of this in [```epl_web_scraper.ipynb```](./epl_web_scraper.ipynb)). We'd aslo have a problem scraping all the goal scorers because the table is **paginated**. So..we know the data in the table is **dynamically loaded**, and a **simple http request** of the html is **not enough**.

**All this means it's time to break out the headless browser, automate with watir, parse tables with pandas, sit back..and enjoy** 👻🤖🐼💅

### Getting Started

> Duplicate the project on **Deepnote** (See launch in Deepnote button at **top** of Readme), **or**, fork this repo to clone in a **local** Python environment e.g.

```bash
$ git clone git@github.com:githubusername/epl_web_scraper.git && cd epl_web_scraper
```

#### ```Dependencies```

> If on **Deepnote**, please see the **```init.ipynb``` (environment tab)** to see how the project is setup. If setting up **locally**, make sure you install **```jupyter```** if you want to use the notebook version. See [the docs](https://docs.pipenv.org/) for help on ```pipenv``` (if not familiar) e.g.

```bash
$ pip install --user pipenv
$ pipenv install jupyter
```

> And install **Chrome Driver**. See [SeleniumHQ wiki](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) e.g.

```bash
# Linux (WSL TBC)
$ sudo apt-get update
$ sudo apt-get install chromium-driver -y

# MacOS w/ Homebrew (See https://brew.sh/)
$ brew tap homebrew/cask && brew cask install chromedriver
```

#### ```Running```

> You have the option to either run the **script (```.py```)** version of the scraper or the **notebook (```.ipynb```)** version of the web scraper. e.g. to run script:

```bash
$ python epl_web_scraper.py
# or with pipenv
$ pipenv run python epl_web_scraper.py
```

#### ```Contributing```

> See [contributing.md](./contributing.md).
