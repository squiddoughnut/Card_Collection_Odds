# --- Configuration Variables (Update these based on the game's RewardState.json file) ---
# Series 4 & 5 lists
unobtained_series_45_cards = [
    "CardSage",
    "CardLegion",
    "CardAjax",
    "CardHydraBob",
    "CardGrandMaster",
    "CardValentina",
    "CardJeanGrey",
    "CardGalactus",
    "CardSupergiant",
    "CardMakkari",
    "CardWiccan",
    "CardThena",
    "CardGwenpool",
    "CardKittyPryde",
    "CardBlob",
    "CardThePhoenixForce",
    "CardNamora",
    "CardDarkHawk",
    "CardIronLad",
    "CardBlackKnight",
    "CardCullObsidian",
    "CardBlackSwan",
    "CardHulkling",
    "CardNicoMinoru",
    "CardUSAgent",
    "CardMisery",
    "CardAgentVenom",
    "CardSurtur",
    "CardScarletSpider",
    "CardHitMonkey",
    "CardKang",
    "CardGladiator",
    "CardScorn",
    "CardThanos",
    "CardMockingbird",
    "CardWarMachine",
    "CardAnnihilus",
    "CardSpeed",
    "CardArishem",
    "CardBaronZemo",
    "CardElsaBloodstone",
    "CardFrigga",
    "CardCorvusGlaive",
    "CardAgony",
    "CardSebastianShaw",
    "CardCaiera",
    "CardMarvelBoy",
    "CardRedGuardian",
    "CardLunaSnow",
    "CardPhastos",
    "CardLasher",
    "CardCopycat",
    "CardMoonstone",
    "CardNocturne",
    "CardVictoriaHand",
    "CardMadameWeb",
    "CardGalacta",
    "CardWerewolfByNight",
    "CardIronPatriot",
    "CardDaken",
    "CardHighEvolutionary",
    "CardArana",
    "CardProximaMidnight",
    "CardPeniParker",
    "CardToxin",
    "CardRocketAndGroot",
    "CardHopeSummers",
    "CardAntiVenom",
    "CardFenrisWolf",
    "CardSasquatch",
    "CardBruceBanner",
    "CardGilgamesh",
    "CardBullseye",
    "CardDoom2099",
    "CardAres",
    "CardLivingTribunal",
    "CardThaddeusRoss",
    "CardRedHulk",
    "CardMiek",
    "CardBlink",
    "CardJoaquinTorres",
    "CardKingEitri",
    "CardScream",
    "CardMalekith"
  ]

past_token_shop_cards = [ # ' "TokenShopCardsSeries4Box": [ '
    "CardHighEvolutionary",
    "CardRedHulk",
    "CardMalekith",
    "CardAntiVenom",
    "CardRedGuardian",
    "CardMiek",
    "CardSasquatch",
    "CardLegion",
    "CardThaddeusRoss",
    "CardGwenpool",
    "CardDaken",
    "CardBaronZemo",
    "CardSage",
    "CardGrandMaster",
    "CardValentina",
    "CardGalacta",
    "CardThanos",
    "CardSupergiant",
    "CardAnnihilus",
    "CardAjax",
    "CardHulkling",
    "CardNicoMinoru",
    "CardHydraBob",
    "CardFrigga",
    "CardMisery"
	]

wanted_series_45_cards = [
    "CardSage"
]
# Series 3 lists
unobtained_series_3_cards = [
    "CardNebula",
    "CardSpiderHam",
    "CardEcho",
    "CardGhostSpider",
    "CardHumanTorch",
    "CardSelene",
    "CardZabu",
    "CardHavok",
    "CardMasterMold",
    "CardMysterio",
    "CardSilk",
    "CardMagik",
    "CardDebrii",
    "CardGambit",
    "CardShanna",
    "CardHercules",
    "CardGhostRider",
    "CardLockjaw",
    "CardSilverSamurai",
    "CardTyphoidMary",
    "CardValkyrie",
    "CardBlackPanther",
    "CardBlackBolt",
    "CardLadyDeathstrike",
    "CardModok",
    "CardJaneFoster",
    "CardRedSkull",
    "CardArnimZola",
    "CardSheHulk"
    ]

past_free_series_3_cards = [ # ' "TokenShopCardsSeries3Box": [ '
    "CardLockjaw",
    "CardBlackPanther",
    "CardJaneFoster",
    "CardMagik",
    "CardSilverSamurai",
    "CardEcho",
    "CardGambit",
    "CardRedSkull",
    "CardTyphoidMary",
    "CardDebrii",
    "CardMasterMold",
    "CardValkyrie",
    "CardMysterio",
    "CardBlackBolt",
    "CardHumanTorch",
    "CardShanna"
    ]

wanted_series_3_cards = [
    "CardJaneFoster",
    "CardMagik",
    "CardArnimZola",
    "CardBlackPanther"
]

# Functions
def avg_draws_needed(remaining_deck_size, remaining_wanted_count):
    """
    Calculate the expected number of draws needed to see a specific number of wanted cards.
    
    Args:
        remaining_deck_size: Total number of cards left to pull
        remaining_wanted_count: Number of wanted cards to see
        
    Returns:
        Expected number of draws needed, rounded to 2 decimal places
    
    Raises:
        ValueError: If wanted cards exceed deck size
    """
    if remaining_wanted_count > remaining_deck_size:
        raise ValueError('Wanted cards cannot exceed all cards size')
    
    total_expected = 0
    
    while remaining_wanted_count > 0:
        expected = (remaining_deck_size + 1) / (remaining_wanted_count + 1)
        total_expected += expected

        remaining_deck_size -= expected
        remaining_wanted_count -= 1
    
    return round(total_expected, 2)

def get_remaining_wanted_cards(wanted_cards, all_cards, seen_cards):
    """
    Determine which wanted cards are still available to collect.
    
    Args:
        wanted_cards: List of cards the user wants
        all_cards: List of all cards in the set
        seen_cards: List of cards already seen
        
    Returns:
        List of wanted cards that have not been shown
    """
    remaining_cards = list(set(all_cards) - set(seen_cards))
    remaining_wanted = [item for item in wanted_cards if item in remaining_cards]

    return remaining_wanted

def calculate_collection_stats(all_cards, seen_cards, wanted_cards, pulls_per_day=3, series_name=""):
    """
    Calculate and display statistics about card collection progress.
    
    Args:
        all_cards: List of all cards in the series
        seen_cards: List of cards already seen
        wanted_cards: List of specific cards the user wants
        pulls_per_day: Number of cards that can be seen per day
        series_name: Name of the card series for display purposes
    """
    total_cards = len(all_cards)
    past_cards_count = len(seen_cards)
    wanted_cards_count = len(wanted_cards)
    available_cards = total_cards - past_cards_count
    
    remaining_wanted = get_remaining_wanted_cards(wanted_cards, all_cards, seen_cards)
    wanted_count = len(remaining_wanted)
    
    # Calculate odds and timeframes
    odds_percentage = round((wanted_count / available_cards) * 100, 2) if available_cards > 0 else 0
    days_till_wanted = round(avg_draws_needed(available_cards, wanted_count) / pulls_per_day, 1)
    days_till_complete = round(available_cards / pulls_per_day, 1)
    days_per_cycle = round(total_cards / pulls_per_day, 1)
    
    # Display results
    print(f'I am missing {total_cards} {series_name} cards.')
    print(f'I want {wanted_cards_count} {series_name} cards,')
    print(f"{', '.join(map(str, wanted_cards))}")
    print()

    if wanted_count == 0:
        print(f'There are {available_cards} {series_name} cards left to pull and I am not looking for any of them.')
    else:
        print(f'There are {available_cards} {series_name} cards left to pull and I am looking for {wanted_count} of them.')
        print(f"{', '.join(map(str, remaining_wanted))}")
        print(f'The odds of pulling a card I want on the next pull is {odds_percentage}%.')
        print(f'With {pulls_per_day} pulls per day, it will take an average of {days_till_wanted} more days to pull my wanted cards.')
    
    print(f'And it will take {days_till_complete} more days to pull all the remaining {series_name} cards.')
    print(f'Finally, it takes {days_per_cycle} days to show all unobtained cards from {series_name}.')

def calculate_series3_completion(total_cards, cards_per_set=4, levels_per_set=108):
    """
    Calculate credits needed to complete Series 3.
    
    Args:
        total_cards: Number of cards needed to complete the series
        cards_per_set: Number of cards earned per set of 9 Collectors Reserves
        levels_per_set: Number of levels needed to earn a set of 9 Collectors Reserves
    """
    collection_level_req = (total_cards / cards_per_set) * levels_per_set
    credits_req = collection_level_req * 50 # 50 credits per level
    
    print(f'I will be series 3 complete after gaining {collection_level_req:,.0f} collection level.')
    print(f'This will take about {credits_req:,.0f} credits.')

def main():
    try:
        print()
        
        # Calculate and display Series 4 & 5 stats
        calculate_collection_stats(
            unobtained_series_45_cards,
            past_token_shop_cards,
            wanted_series_45_cards,
            pulls_per_day=3,
            series_name="series 4 and series 5"
        )
        print()

        # Calculate and display Series 3 stats
        calculate_collection_stats(
            unobtained_series_3_cards,
            past_free_series_3_cards,
            wanted_series_3_cards,
            pulls_per_day=3,
            series_name="series 3"
        )
        print()

        # Calculate Series 3 completion resources
        calculate_series3_completion(len(unobtained_series_3_cards))
        print()
    except ValueError as e:
        print(f"Error in calculations: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero occurred. This might happen if there are no available cards left.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()