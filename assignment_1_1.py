def is_older(my_age, brother_age, sister_age):
    # Ulozte do promenne vysledek logicke operace "Jste mladsi nez Vas bratr?"
    is_older_a = my_age < brother_age
    print(f"Are you younger than your brother? {is_older_a}")

    # Ulozte do promenne vysledek logicke operace "Je Vas bratr starsi nez Vase sestra?"
    is_older_b = ...
    print(f"Is your brother older than your sister? {is_older_b}")

    # Ulozte do promenne vysledek logicke operace "Je Vase setra zaroven mladsi nez Vy i nez Vas bratr?"
    is_older_c = ...
    print(f"Is your sister younger than both you and your brother? {is_older_c}")

    # Ulozte do promenne vysledek logicke operace "Jste mladsi nez alespon jeden z Vasich sourozencu?"
    is_older_d = ...
    print(f"Are you younger than at least one of your siblings? {is_older_d}")

    # Ulozte do promenne vysledek logicke operace "Bratr neni starsi nez ja a sestra dohromady."
    is_older_e = ...
    print(f"My brother is not older than me and my sister combined. {is_older_e}")

    return is_older_a, is_older_b, is_older_c, is_older_d, is_older_e


if __name__ == "__main__":
    my_age = ...
    brother_age = ...
    sister_age = ...

    is_older(my_age, brother_age, sister_age)
