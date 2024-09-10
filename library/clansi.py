class Clansi:
    """ANSI escape sequences for colour and style in terminal output."""
    # Reset all styles
    _reset = "\033[0m"
    # Styles
    _bold = "\033[1m"
    _dim = "\033[2m"
    _underline = "\033[4m"
    _blink = "\033[5m"
    _reverse = "\033[7m"
    _hidden = "\033[8m"
    # Foreground colours
    _black = "\033[30m"
    _red = "\033[31m"
    _green = "\033[32m"
    _yellow = "\033[33m"
    _blue = "\033[34m"
    _magenta = "\033[35m"
    _cyan = "\033[36m"
    _white = "\033[37m"
    # Background colours
    _black_bg = "\033[40m"
    _red_bg = "\033[41m"
    _green_bg = "\033[42m"
    _yellow_bg = "\033[43m"
    _blue_bg = "\033[44m"
    _magenta_bg = "\033[45m"
    _cyan_bg = "\033[46m"
    _white_bg = "\033[47m"
    # Bright foreground colours
    _black_bright = "\033[90m"
    _red_bright = "\033[91m"
    _green_bright = "\033[92m"
    _yellow_bright = "\033[93m"
    _blue_bright = "\033[94m"
    _magenta_bright = "\033[95m"
    _cyan_bright = "\033[96m"
    _white_bright = "\033[97m"
    # Bright background colours
    _black_bg_bright = "\033[100m"
    _red_bg_bright = "\033[101m"
    _green_bg_bright = "\033[102m"
    _yellow_bg_bright = "\033[103m"
    _blue_bg_bright = "\033[104m"
    _magenta_bg_bright = "\033[105m"
    _cyan_bg_bright = "\033[106m"
    _white_bg_bright = "\033[107m"

    @staticmethod
    def _format_text(formats: list, text: str) -> str:
        """Format text with ANSI escape sequences
            :param formats: List of formats
                :type formats: list
            :param text: Text to format
                :type text: str
            :return: Formatted text
                :rtype: str
        """
        return f'{"".join(formats)}{text}{Clansi._reset}'

    @staticmethod
    def _apply_colour(text: str, colour: str,
                      bold: bool, underline: bool, blink: bool, reverse: bool, hidden: bool) -> str:
        """Add Ansi sign to colour text or its background. Set some styles if needed.
            :param text: Text to colour
                :type text: str
            :param colour: Colour to use
                :type colour: str
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Coloured text
                :rtype: str
        """
        formats = Clansi._flag_to_format_list(bold, underline, blink, reverse, hidden)
        if not formats:
            return Clansi._format_text([colour], text)
        return Clansi._format_text(formats.append(colour), text)

    @staticmethod
    def _flag_to_format_list(bold: bool, underline: bool, blink: bool, reverse: bool, hidden: bool) -> list:
        """Convert flags to format list
            :param bold: Bold flag
                :type bold: bool
            :param underline: Underline flag
                :type underline: bool
            :param blink: Blink flag
                :type blink: bool
            :param reverse: Reverse flag
                :type reverse: bool
            :param hidden: Hidden flag
                :type hidden: bool
            :return: List of formats
                :rtype: list
        """
        formats = []
        if bold:
            formats.append(Clansi._bold)
        if underline:
            formats.append(Clansi._underline)
        if blink:
            formats.append(Clansi._blink)
        if reverse:
            formats.append(Clansi._reverse)
        if hidden:
            formats.append(Clansi._hidden)
        return formats

    @staticmethod
    def bold(text: str) -> str:
        """Bold text
            :param text: Text to bold
                :type text: str
            :return: Bold text
                :rtype: str
        """
        return Clansi._format_text([Clansi._bold], text)

    @staticmethod
    def dim(text: str) -> str:
        """Dim text
            :param text: Text to dim
                :type text: str
            :return: Dim text
                :rtype: str
        """
        return Clansi._format_text([Clansi._dim], text)

    @staticmethod
    def underline(text: str) -> str:
        """Underline text
            :param text: Text to underline
                :type text: str
            :return: Underlined text
                :rtype: str
        """
        return Clansi._format_text([Clansi._underline], text)

    @staticmethod
    def blink(text: str) -> str:
        """Blink text
            :param text: Text to blink
                :type text: str
            :return: Blinking text
                :rtype: str
        """
        return Clansi._format_text([Clansi._blink], text)

    @staticmethod
    def reverse(text: str) -> str:
        """Reverse text
            :param text: Text to reverse
                :type text: str
            :return: Reversed text
                :rtype: str
        """
        return Clansi._format_text([Clansi._reverse], text)

    @staticmethod
    def hidden(text: str) -> str:
        """Hidden text
            :param text: Text to hide
                :type text: str
            :return: Hidden text
                :rtype: str
        """
        return Clansi._format_text([Clansi._hidden], text)

    @staticmethod
    def black(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
              blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Black text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Black text
                :rtype: str
        """
        colour = Clansi._black_bright if bright else Clansi._black
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def red(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
            blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Red text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Red text
                :rtype: str
        """
        colour = Clansi._red_bright if bright else Clansi._red
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def green(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
              blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Green text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Green text
                :rtype: str
        """
        colour = Clansi._green_bright if bright else Clansi._green
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def yellow(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
               blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Yellow text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Yellow text
                :rtype: str
        """
        colour = Clansi._yellow_bright if bright else Clansi._yellow
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def blue(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
             blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Blue text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Blue text
                :rtype: str
        """
        colour = Clansi._blue_bright if bright else Clansi._blue
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def magenta(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Magenta text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Magenta text
                :rtype: str
        """
        colour = Clansi._magenta_bright if bright else Clansi._magenta
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def cyan(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
             blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Cyan text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Cyan text
                :rtype: str
        """
        colour = Clansi._cyan_bright if bright else Clansi._cyan
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def white(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
              blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """White text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: White text
                :rtype: str
        """
        colour = Clansi._white_bright if bright else Clansi._white
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def black_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                 blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Black background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Black background text
                :rtype: str
        """
        colour = Clansi._black_bg_bright if bright else Clansi._black_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def red_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
               blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Red background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Red background text
                :rtype: str
        """
        colour = Clansi._red_bg_bright if bright else Clansi._red_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def green_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                 blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Green background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Green background text
                :rtype: str
        """
        colour = Clansi._green_bg_bright if bright else Clansi._green_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def yellow_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                  blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Yellow background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Yellow background text
                :rtype: str
        """
        colour = Clansi._yellow_bg_bright if bright else Clansi._yellow_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def blue_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Blue background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Blue background text
                :rtype: str
        """
        colour = Clansi._blue_bg_bright if bright else Clansi._blue_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def magenta_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                   blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Magenta background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Magenta background text
                :rtype: str
        """
        colour = Clansi._magenta_bg_bright if bright else Clansi._magenta_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def cyan_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """Cyan background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: Cyan background text
                :rtype: str
        """
        colour = Clansi._cyan_bg_bright if bright else Clansi._cyan_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)

    @staticmethod
    def white_bg(text: str, bright: bool = False, bold: bool = False, underline: bool = False,
                 blink: bool = False, reverse: bool = False, hidden: bool = False) -> str:
        """White background text
            :param text: Text to colour
                :type text: str
            :param bright: Use bright colour
                :type bright: bool
            :param bold: Bold text
                :type bold: bool
            :param underline: Underline text
                :type underline: bool
            :param blink: Blink text
                :type blink: bool
            :param reverse: Reverse text
                :type reverse: bool
            :param hidden: Hidden text
                :type hidden: bool
            :return: White background text
                :rtype: str
        """
        colour = Clansi._white_bg_bright if bright else Clansi._white_bg
        return Clansi._apply_colour(text, colour, bold, underline, blink, reverse, hidden)