from pygame import mixer


class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True

        self.soundtrack = mixer.Sound("./sound_effects/main_theme.ogg")
        self.coin = mixer.Sound("./sound_effects/coin.ogg")
        self.bump = mixer.Sound("./sound_effects/bump.ogg")
        self.stomp = mixer.Sound("./sound_effects/stomp.ogg")
        self.jump = mixer.Sound("./sound_effects/small_jump.ogg")
        self.death = mixer.Sound("./sound_effects/death.wav")
        self.kick = mixer.Sound("./sound_effects/kick.ogg")
        self.brick_bump = mixer.Sound("./sound_effects/brick-bump.ogg")
        self.powerup = mixer.Sound('./sound_effects/powerup.ogg')
        self.powerup_appear = mixer.Sound('./sound_effects/powerup_appears.ogg')
        self.pipe = mixer.Sound('./sound_effects/pipe.ogg')

    def play_sfx(self, sound_effects):
        if self.allowSFX:
            self.sfx_channel.play(sound_effects)

    def play_music(self, music):
        self.music_channel.play(music)
