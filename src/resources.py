""" For loading resources.
    Style borrowed from example game made by Pygame community - stuntcat
"""
import os
import pygame
_sfx_cache = {}
_gfx_cache = {}

_font_cache = {}


def data_path():
    if os.path.exists('../media'):
        path = '../media'
    else:
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'media',
        )
    return path


def music(music_name=None, load=True, play=True, stop=False):
    """ For loading and playing music.
    ::Example::
    music('bla.ogg', load=True, play=True)
    music(stop=True)
    """
    # perhaps the mixer is not included or initialised.
    if pygame.mixer and pygame.mixer.get_init():
        if load and not stop:
            pygame.mixer.music.load(music_path(music_name))
        if play and stop is None or stop is False:
            pygame.mixer.music.play()
        elif stop:
            pygame.mixer.music.stop()


def music_path(music_name):
    path = os.path.join(data_path(), '', music_name)
    return path


def gfx(image, convert=False, convert_alpha=False):
    """
    Lazily loads graphics
    :param image:
    :param convert:
    :param convert_alpha:
    :return:
    """
    global _gfx_cache
    gfx_key = (image, convert, convert_alpha)
    if gfx_key in _gfx_cache:
        return _gfx_cache[gfx_key]

    path = os.path.join(data_path(), '', image)
    asurf = pygame.image.load(path)
    _gfx_cache[gfx_key] = asurf
    return asurf


def sfx(snd, play=False, stop=False):
    global _sfx_cache
    snd_key = snd
    if snd_key in _sfx_cache:
        got_sound = _sfx_cache[snd_key]
    else:
        path = os.path.join(data_path(), '', snd)
        got_sound = pygame.mixer.Sound(path)
        _sfx_cache[snd_key] = got_sound

    # print(snd_key, play, stop, time.time())
    if play:
        got_sound.play()
    if stop:
        got_sound.stop()
    return got_sound


def font(fnt, text_size):
    global _font_cache
    font_key = (fnt, text_size)
    if font_key in _font_cache:
        return _font_cache[font_key]

    path = os.path.join(data_path(), '', fnt)
    got_font = pygame.font.Font(path, text_size)
    _font_cache[font_key] = got_font
    return got_font