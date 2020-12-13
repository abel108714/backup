def create_fonts( self ):
        '''
        Create all font objects
        '''
        self.known_fonts = {}
        def handle_font( font_config, text_metric, font_type, param ):
            #print font_config.lfFaceName
            self.known_fonts[ font_config.lfFaceName ] = font_config
            return True

        hdc = win32gui.GetWindowDC( self.main_window.window_handle )
        
        #print "=== begin availalbe fonts ==="
        win32gui.EnumFontFamilies( hdc, None, handle_font, None )
        #print "=== end available fonts ==="

        # https://stackoverflow.com/questions/6057239/which-font-is-the-default-for-mfc-dialog-controls
        self.non_client_metrics = win32gui.SystemParametersInfo( win32con.SPI_GETNONCLIENTMETRICS, None, 0 )
        self.default_font = self.non_client_metrics[ 'lfMessageFont' ].lfFaceName
        
        #print "Default font: " + self.default_font
        keys = ( 'title', 'details', 'notification', 'splash', 'buttons' )
        font_config = self.config.get( 'font_styles', {} )
        self.fonts = { key: self.create_font( hdc, **font_config.get(key, {}) ) for key in keys }
        if 'buttons' not in self.fonts:
            self.fonts['buttons'] = win32gui.CreateFontIndirect( self.non_client_metrics[ 'lfMessageFont' ] )

        win32gui.ReleaseDC( self.main_window.window_handle, hdc ) 