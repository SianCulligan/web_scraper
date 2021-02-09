from web_scraper import __version__
from web_scraper.scrapper import get_citations_needed_count, get_citations_needed_report, url, for_testing



def test_version():
    assert __version__ == '0.1.0'

# verify_that_correct_count_of_citations_needed_is_calculated
# verify_that_preceding_passage

def test_can_get_the_correct_count_of_citations():
    expected = 4
    actual = get_citations_needed_count(url)
    assert expected == actual

def test_can_verify_preceding_passage():
    expected = for_testing
    actual = get_citations_needed_report(url)
    assert expected == actual





# for_test = """Coffee may be brewed by steeping in a device such as a French press (also known as a cafetière, coffee press or coffee plunger).[109] Ground coffee and hot water are combined in a cylindrical vessel and left to brew for a few minutes. A circular filter which fits tightly in the cylinder fixed to a plunger is then pushed down from the top to force the grounds to the bottom. The filter retains the grounds at the bottom as the coffee is poured from the container. Because the coffee grounds are in direct contact with the water, all the coffee oils remain in the liquid, making it a stronger beverage. This method of brewing leaves more sediment than in coffee made by an automatic coffee machine.[109] Supporters of the French press method point out that the sediment issue can be minimized by using the right type of grinder: they claim that a rotary blade grinder cuts the coffee bean into a wide range of sizes, including a fine coffee dust that remains as sludge at the bottom of the cup, while a burr grinder uniformly grinds the beans into consistently-sized grinds, allowing the coffee to settle uniformly and be trapped by the press.[110] Within the first minute of brewing 95% of the caffeine is released from the coffee bean.[citation needed]
# \n
# \n
# A number of products are sold for the convenience of consumers who do not want to prepare their own coffee or who do not have access to coffeemaking equipment. Instant coffee is dried into soluble powder or freeze-dried into granules that can be quickly dissolved in hot water.[123] Originally invented in 1907,[124][125] it rapidly gained in popularity in many countries in the post-war period, with Nescafé being the most popular product.[126] Many consumers determined that the convenience in preparing a cup of instant coffee more than made up for a perceived inferior taste,[127] although, since the late 1970s, instant coffee has been produced differently in such a way that is similar to the taste of freshly brewed coffee.[citation needed] Paralleling (and complementing) the rapid rise of instant coffee was the coffee vending machine invented in 1947 and widely distributed since the 1950s.[128]
# \n
# \n
# Coffee is often consumed alongside (or instead of) breakfast by many at home or when eating out at diners or cafeterias. It is often served at the end of a formal meal, normally with a dessert, and at times with an after-dinner mint, especially when consumed at a restaurant or dinner party.[citation needed]
# \n
# \n
# Ethiopian Orthodox Christians prohibited coffee, regarded as a Muslim drink, until as late as 1889; as of 2019[update] it is considered[by whom?] a national drink of Ethiopia for people of all faiths.[citation needed] In 1670 some French doctors condemned coffee as poisonous.[219]
# Coffee's early association in Europe with rebellious political activities led to King Charles II of England outlawing coffeehouses from January 1676 (although the subsequent uproar forced the monarch to back down two days before the ban was due to come into force).[29] King Frederick the Great banned it in Prussia in 1777 for nationalistic and economic reasons; concerned about the price of imports, he sought to force the public back to consuming beer.[220] Lacking coffee-producing colonies, Prussia had to import all its coffee at a great cost.[221]
# \n
# \n
# """