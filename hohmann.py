#!/usr/bin/env python3
"""Calculateur de transfert de Hohmann entre deux orbites circulaires terrestres."""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


MU_TERRE_KM3_S2 = 398_600.4418
RAYON_TERRE_KM = 6_378.1363


@dataclass(frozen=True)
class ResultatHohmann:
    altitude_depart_km: float
    altitude_arrivee_km: float
    rayon_depart_km: float
    rayon_arrivee_km: float
    delta_v_depart_km_s: float
    delta_v_arrivee_km_s: float
    delta_v_total_km_s: float
    duree_transfert_s: float


def calculer_transfert(altitude_depart_km: float, altitude_arrivee_km: float) -> ResultatHohmann:
    """Calcule le transfert de Hohmann idéal entre deux orbites circulaires.

    Les altitudes sont mesurées au-dessus de la surface terrestre. Les orbites
    doivent être au-dessus de la Terre et de rayons distincts.
    """
    valeurs = (altitude_depart_km, altitude_arrivee_km)
    if not all(math.isfinite(valeur) for valeur in valeurs):
        raise ValueError("Les altitudes doivent être des nombres finis.")
    if any(altitude < 0 for altitude in valeurs):
        raise ValueError("Les altitudes ne peuvent pas être négatives.")
    if math.isclose(altitude_depart_km, altitude_arrivee_km, abs_tol=1e-12):
        raise ValueError("Les orbites de départ et d'arrivée doivent être différentes.")

    r1 = RAYON_TERRE_KM + altitude_depart_km
    r2 = RAYON_TERRE_KM + altitude_arrivee_km
    demi_grand_axe = (r1 + r2) / 2

    vitesse_circulaire_depart = math.sqrt(MU_TERRE_KM3_S2 / r1)
    vitesse_circulaire_arrivee = math.sqrt(MU_TERRE_KM3_S2 / r2)
    vitesse_perigee_transfert = math.sqrt(
        MU_TERRE_KM3_S2 * (2 / r1 - 1 / demi_grand_axe)
    )
    vitesse_apogee_transfert = math.sqrt(
        MU_TERRE_KM3_S2 * (2 / r2 - 1 / demi_grand_axe)
    )

    dv_depart = abs(vitesse_perigee_transfert - vitesse_circulaire_depart)
    dv_arrivee = abs(vitesse_circulaire_arrivee - vitesse_apogee_transfert)
    duree = math.pi * math.sqrt(demi_grand_axe**3 / MU_TERRE_KM3_S2)

    return ResultatHohmann(
        altitude_depart_km=altitude_depart_km,
        altitude_arrivee_km=altitude_arrivee_km,
        rayon_depart_km=r1,
        rayon_arrivee_km=r2,
        delta_v_depart_km_s=dv_depart,
        delta_v_arrivee_km_s=dv_arrivee,
        delta_v_total_km_s=dv_depart + dv_arrivee,
        duree_transfert_s=duree,
    )


def formater_duree(secondes: float) -> str:
    heures = secondes / 3600
    jours = heures / 24
    if jours >= 1:
        return f"{jours:,.2f} jours ({heures:,.1f} h)"
    return f"{heures:,.2f} h"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calcule le delta-v et la durée d'un transfert de Hohmann terrestre."
    )
    parser.add_argument("altitude_depart", type=float, help="Altitude de l'orbite de départ (km)")
    parser.add_argument("altitude_arrivee", type=float, help="Altitude de l'orbite d'arrivée (km)")
    args = parser.parse_args()

    try:
        resultat = calculer_transfert(args.altitude_depart, args.altitude_arrivee)
    except ValueError as erreur:
        parser.error(str(erreur))

    print("\n TRANSFERT DE HOHMANN — TERRE")
    print("─" * 38)
    print(f"Orbite de départ   : {resultat.altitude_depart_km:,.1f} km d'altitude")
    print(f"Orbite d'arrivée   : {resultat.altitude_arrivee_km:,.1f} km d'altitude")
    print(f"Impulsion au départ: {resultat.delta_v_depart_km_s:.3f} km/s")
    print(f"Impulsion arrivée  : {resultat.delta_v_arrivee_km_s:.3f} km/s")
    print(f"Delta-v total      : {resultat.delta_v_total_km_s:.3f} km/s")
    print(f"Durée du transfert : {formater_duree(resultat.duree_transfert_s)}")
    print("\nModèle idéal à deux corps : manœuvres impulsionnelles, sans perturbations.")


if __name__ == "__main__":
    main()
