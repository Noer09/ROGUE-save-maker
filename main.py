from CaesarCipher import coder

def main():
    # Save file located at: <csgo_base_dir>/cfg/rogue_savefile_slot0.log
    # q: The point upgrades system (XP upgrades are saved in this dictionary)
    # -- p: Weapons set 4   (MAX: 27500)
    # -- r: Cards set 3     (MAX: 27500)
    # -- u: Weapons set 1   (MAX: 15500)
    # -- t: Cards set 4     (MAX: 27500)
    # -- w: Cards set 1     (MAX: 27500)
    # -- i: Weapons set 2   (MAX: 15500)
    # -- h: Doors upgrades  (MAX: 100)
    # -- j: Location set 1  (MAX: 27500)
    # -- z: Money set       (MAX: 27500)
    # -- e: Cards set 2     (MAX: 27500)
    # -- o: Weapons set 3   (MAX: 27500)
    # -- y: Cards set 5     (MAX: 27500)
    # x:    Total amount of runs
    # c:    Seed in ASCII values (https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html)
    # xp:   Amount of XP unused
    # f:    Amount of time used in the most recent VR session (set in seconds)
    # g:    The total amount of time used in VR sessions (set in seconds)
    # n:    Booster packs given as combined power 2^x as flag (MAX: 16383)
    #
    # Flags of all booster packs
    # -- 1    (2^0) : incubator
    # -- 2    (2^1) : chickenlord
    # -- 4    (2^2) : punchline
    # -- 8    (2^3) : exoticmadness
    # -- 16   (2^4) : superpunch
    # -- 32   (2^5) : dance
    # -- 64   (2^6) : shotgun_to_death
    # -- 128  (2^7) : secondaidkit
    # -- 256  (2^8) : hedgehog
    # -- 512  (2^9) : snipermaster
    # -- 1024 (2^10): athlete
    # -- 2048 (2^11): oldwounds
    # -- 4096 (2^12): explosiveman
    # -- 8192 (2^13): free_wf
    save = coder.encode(
        "{"
            "q={"
                "p=0,"
                "r=0,"
                "u=0,"
                "t=0,"
                "w=0,"
                "i=0,"
                "h=0,"
                "j=0,"
                "z=0,"
                "e=0,"
                "o=0,"
                "y=0"
            "},"
            "x=0,"
            "c=Unchar([70,73,82,83,84,82,85,78]),"
            "xp=0,"
            "f=0,"
            "g=0,"
            "n=0"
        "}")

    print(save+",L="+str(len(save)))

if __name__ == "__main__":
    main()
