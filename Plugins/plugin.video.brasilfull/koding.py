# -*- coding: utf-8 -*-
import urllib
import urllib2
import datetime
import re
import os
import base64
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
import time
import requests
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
__addon__ = xbmcaddon . Addon ( )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
__icon__ = __addon__ . getAddonInfo ( 'icon' )
if 73 - 73: II111iiii
IiII1IiiIiI1 = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'docs.google.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
iIiiiI1IiI1I1 = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' , 'plugin://plugin.video.youtube/kodion/search/input' , 'plugin.video.quasar/search' ]
if 87 - 87: OoOoOO00
class I11i ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
I11iIi1I = xbmcaddon . Addon ( id = 'plugin.video.brasilfull' )
IiiIII111iI = I11iIi1I . getAddonInfo ( 'version' )
IiII = xbmc . translatePath ( I11iIi1I . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iI1Ii11111iIi = xbmc . translatePath ( I11iIi1I . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
i1i1II = os . path . join ( IiII , 'favorites' )
O0oo0OO0 = os . path . join ( IiII , 'history' )
I1i1iiI1 = I11iIi1I . getSetting ( 'plugin' )
iiIIIII1i1iI = os . path . join ( IiII , 'list_revision' )
o0oO0 = os . path . join ( iI1Ii11111iIi , 'icon.png' )
oo00 = os . path . join ( iI1Ii11111iIi , 'fanart.jpg' )
o00 = os . path . join ( IiII , 'source_file' )
Oo0oO0ooo = IiII
if 56 - 56: ooO00oOoo - O0OOo
downloader = downloader . SimpleDownloader ( )
II1Iiii1111i = I11iIi1I . getSetting ( 'debug' )
if os . path . exists ( i1i1II ) == True :
 i1IIi11111i = open ( i1i1II ) . read ( )
else : i1IIi11111i = [ ]
if os . path . exists ( o00 ) == True :
 o000o0o00o0Oo = open ( o00 ) . read ( )
else : o000o0o00o0Oo = [ ]
if 80 - 80: i1iII1I1i1i1 . i1iIIII
def I1 ( string ) :
 if II1Iiii1111i == 'true' :
  xbmc . log ( "[addon.live.BrasilFull Lists-%s]: %s" % ( IiiIII111iI , string ) )
  if 54 - 54: oO % IiiIIiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
def ii11iIi1I ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'BrasilFull/3.0' }
  iI111I11I1I1 = urllib2 . Request ( url , None , headers )
  OOooO0OOoo = urllib2 . urlopen ( iI111I11I1I1 )
  iIii1 = OOooO0OOoo . read ( )
  OOooO0OOoo . close ( )
  return iIii1
 except urllib2 . URLError , oOOoO0 :
  I1 ( 'URL: ' + url )
  if hasattr ( oOOoO0 , 'code' ) :
   I1 ( 'Falha de erro - %s.' % oOOoO0 . code )
   xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,Erro de código - " + str ( oOOoO0 . code ) + ",10000," + o0oO0 + ")" )
  elif hasattr ( oOOoO0 , 'reason' ) :
   I1 ( 'Falha ao conectar com o servidor.' )
   I1 ( 'Reason: %s' % oOOoO0 . reason )
   xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,Falha de ao se conectar com o servidor. - " + str ( oOOoO0 . reason ) + ",10000," + o0oO0 + ")" )
   if 59 - 59: oO * i11iIiiIii + oO + i1iIIi1 * i1
def OooOoO0Oo ( ) :
 I1 ( "SKindex" )
 iiIIiIiIi ( i1I11 , '' )
 iI = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x70\x61\x73\x74\x65\x73\x68\x72\x2e\x63\x6f\x6d\x2f\x72\x61\x77\x2f\x79\x42\x54\x49\x61\x47\x53\x6a\x68\x6d"
 o0O00oooo = iI
 O00o = urllib2 . urlopen ( o0O00oooo ) . read ( )
 time = 15000
 xbmc . executebuiltin ( 'Notification(%s, %s, %d, %s)' % ( __addonname__ , O00o , time , __icon__ ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 61 - 61: IiiIIiiI11 . iIii1I11I1II1 * OoOoOO00 . i1iIIi1 % OOooo000oo0
def oOo00Oo00O ( data ) :
 try :
  if data and len ( data ) > 0 and data . startswith ( '$pyFunction:' ) :
   data = iI11i1I1 ( data . split ( '$pyFunction:' ) [ 1 ] , '' , None , None )
 except : pass
 return data
 if 71 - 71: i1iIIi1 % IiiIIiiI11 / IIIiiIIii
def ii11i1iIII ( ) :
 if os . path . exists ( i1i1II ) == True :
  Ii1I ( 'Favorites' , 'url' , 4 , os . path . join ( iI1Ii11111iIi , 'resources' , 'favorite.png' ) , oo00 , '' , '' , '' , '' )
 if I11iIi1I . getSetting ( "browse_xml_database" ) == "true" :
  Ii1I ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/www-data/filesystem/' , 15 , o0oO0 , oo00 , '' , '' , '' , '' )
 if I11iIi1I . getSetting ( "browse_community" ) == "true" :
  Ii1I ( 'Community Files' , 'community_files' , 16 , o0oO0 , oo00 , '' , '' , '' , '' )
 if os . path . exists ( O0oo0OO0 ) == True :
  Ii1I ( 'Search History' , 'history' , 25 , os . path . join ( iI1Ii11111iIi , 'resources' , 'favorite.png' ) , oo00 , '' , '' , '' , '' )
 if I11iIi1I . getSetting ( "searchyt" ) == "true" :
  Ii1I ( 'Search:Youtube' , 'youtube' , 25 , o0oO0 , oo00 , '' , '' , '' , '' )
 if I11iIi1I . getSetting ( "searchDM" ) == "true" :
  Ii1I ( 'Search:dailymotion' , 'dmotion' , 25 , o0oO0 , oo00 , '' , '' , '' , '' )
 if I11iIi1I . getSetting ( "PulsarM" ) == "true" :
  Ii1I ( 'Quasar:IMDB' , 'IMDBidplay' , 27 , o0oO0 , oo00 , '' , '' , '' , '' )
 if os . path . exists ( o00 ) == True :
  Oo0o0 = json . loads ( open ( o00 , "r" ) . read ( ) )
  if len ( Oo0o0 ) > 1 :
   for III1ii1iII in Oo0o0 :
    if isinstance ( III1ii1iII , list ) :
     Ii1I ( III1ii1iII [ 0 ] . encode ( 'utf-8' ) , III1ii1iII [ 1 ] . encode ( 'utf-8' ) , 1 , o0oO0 , oo00 , '' , '' , '' , '' , 'source' )
    else :
     oo0oooooO0 = o0oO0
     i11Iiii = oo00
     iII1i1I1II = ''
     i1IiIiiI = ''
     credits = ''
     I1I = ''
     if III1ii1iII . has_key ( 'thumbnail' ) :
      oo0oooooO0 = III1ii1iII [ 'thumbnail' ]
     if III1ii1iII . has_key ( 'fanart' ) :
      i11Iiii = III1ii1iII [ 'fanart' ]
     if III1ii1iII . has_key ( 'description' ) :
      iII1i1I1II = III1ii1iII [ 'description' ]
     if III1ii1iII . has_key ( 'date' ) :
      i1IiIiiI = III1ii1iII [ 'date' ]
     if III1ii1iII . has_key ( 'genre' ) :
      I1I = III1ii1iII [ 'genre' ]
     if III1ii1iII . has_key ( 'credits' ) :
      credits = III1ii1iII [ 'credits' ]
     Ii1I ( III1ii1iII [ 'title' ] . encode ( 'utf-8' ) , III1ii1iII [ 'url' ] . encode ( 'utf-8' ) , 1 , oo0oooooO0 , i11Iiii , iII1i1I1II , I1I , i1IiIiiI , credits , 'source' )
     if 80 - 80: ii1IiI1i - i1
  else :
   if len ( Oo0o0 ) == 1 :
    if isinstance ( Oo0o0 [ 0 ] , list ) :
     iiIIiIiIi ( Oo0o0 [ 0 ] [ 1 ] . encode ( 'utf-8' ) , oo00 )
    else :
     iiIIiIiIi ( Oo0o0 [ 0 ] [ 'url' ] , Oo0o0 [ 0 ] [ 'fanart' ] )
     if 87 - 87: O0OOo / i1iIIII - i1IIi * i1iII1I1i1i1 / OoooooooOO . O0
     if 1 - 1: II111iiii - i1iIIII / i1iIIII
def I1II1III11iii ( url = None ) :
 if url is None :
  if not I11iIi1I . getSetting ( "new_file_source" ) == "" :
   Oo000 = I11iIi1I . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not I11iIi1I . getSetting ( "new_url_source" ) == "" :
   Oo000 = I11iIi1I . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  Oo000 = url
 if Oo000 == '' or Oo000 is None :
  return
 I1 ( 'Adding New Source: ' + Oo000 . encode ( 'utf-8' ) )
 if 51 - 51: i11iIiiIii . OoOoOO00 + II111iiii
 II111ii1II1i = None
 iIii1 = OoOo00o ( Oo000 )
 print 'source_url' , Oo000
 if isinstance ( iIii1 , BeautifulSOAP ) :
  if iIii1 . find ( 'channels_info' ) :
   II111ii1II1i = iIii1 . channels_info
  elif iIii1 . find ( 'items_info' ) :
   II111ii1II1i = iIii1 . items_info
 if II111ii1II1i :
  o0OOoo0OO0OOO = { }
  o0OOoo0OO0OOO [ 'url' ] = Oo000
  try : o0OOoo0OO0OOO [ 'title' ] = II111ii1II1i . title . string
  except : pass
  try : o0OOoo0OO0OOO [ 'thumbnail' ] = II111ii1II1i . thumbnail . string
  except : pass
  try : o0OOoo0OO0OOO [ 'fanart' ] = II111ii1II1i . fanart . string
  except : pass
  try : o0OOoo0OO0OOO [ 'genre' ] = II111ii1II1i . genre . string
  except : pass
  try : o0OOoo0OO0OOO [ 'description' ] = II111ii1II1i . description . string
  except : pass
  try : o0OOoo0OO0OOO [ 'date' ] = II111ii1II1i . date . string
  except : pass
  try : o0OOoo0OO0OOO [ 'credits' ] = II111ii1II1i . credits . string
  except : pass
 else :
  if '/' in Oo000 :
   iI1iI1I1i1I = Oo000 . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in Oo000 :
   iI1iI1I1i1I = Oo000 . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in iI1iI1I1i1I :
   iI1iI1I1i1I = urllib . unquote_plus ( iI1iI1I1i1I )
  iIi11Ii1 = xbmc . Keyboard ( iI1iI1I1i1I , 'Deseja renomear?' )
  iIi11Ii1 . doModal ( )
  if ( iIi11Ii1 . isConfirmed ( ) == False ) :
   return
  Ii11iII1 = iIi11Ii1 . getText ( )
  if len ( Ii11iII1 ) == 0 :
   return
  o0OOoo0OO0OOO = { }
  o0OOoo0OO0OOO [ 'title' ] = Ii11iII1
  o0OOoo0OO0OOO [ 'url' ] = Oo000
  o0OOoo0OO0OOO [ 'fanart' ] = i11Iiii
  if 51 - 51: II111iiii * i1 % IIIiiIIii * II111iiii % ooO00oOoo / i1iIIi1
 if os . path . exists ( o00 ) == False :
  iIIIIii1 = [ ]
  iIIIIii1 . append ( o0OOoo0OO0OOO )
  oo000OO00Oo = open ( o00 , "w" )
  oo000OO00Oo . write ( json . dumps ( iIIIIii1 ) )
  oo000OO00Oo . close ( )
 else :
  Oo0o0 = json . loads ( open ( o00 , "r" ) . read ( ) )
  Oo0o0 . append ( o0OOoo0OO0OOO )
  oo000OO00Oo = open ( o00 , "w" )
  oo000OO00Oo . write ( json . dumps ( Oo0o0 ) )
  oo000OO00Oo . close ( )
 I11iIi1I . setSetting ( 'new_url_source' , "" )
 I11iIi1I . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,Novos conteúdos adicionados.,5000," + o0oO0 + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : I11iIi1I . openSettings ( )
 if 51 - 51: oooOOOOO * IIIiiIIii + i1iIIII + i1
 if 66 - 66: ii1IiI1i
def oO000Oo000 ( name ) :
 Oo0o0 = json . loads ( open ( o00 , "r" ) . read ( ) )
 for i111IiI1I in range ( len ( Oo0o0 ) ) :
  if isinstance ( Oo0o0 [ i111IiI1I ] , list ) :
   if Oo0o0 [ i111IiI1I ] [ 0 ] == name :
    del Oo0o0 [ i111IiI1I ]
    oo000OO00Oo = open ( o00 , "w" )
    oo000OO00Oo . write ( json . dumps ( Oo0o0 ) )
    oo000OO00Oo . close ( )
    break
  else :
   if Oo0o0 [ i111IiI1I ] [ 'title' ] == name :
    del Oo0o0 [ i111IiI1I ]
    oo000OO00Oo = open ( o00 , "w" )
    oo000OO00Oo . write ( json . dumps ( Oo0o0 ) )
    oo000OO00Oo . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 70 - 70: oO . OOooo000oo0 / IIIiiIIii . oO - O0 / oooOOOOO
 if 62 - 62: iIii1I11I1II1 * ii1IiI1i
 if 26 - 26: IiiIIiiI11 . IiiIII111ii
def oOOOOo0 ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 iiII1i1 = BeautifulSoup ( ii11iIi1I ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for III1ii1iII in iiII1i1 ( 'a' ) :
  o00oOO0o = III1ii1iII [ 'href' ]
  if not o00oOO0o . startswith ( '?' ) :
   OOO00O = III1ii1iII . string
   if OOO00O not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if o00oOO0o . endswith ( '/' ) :
     if browse :
      Ii1I ( OOO00O , url + o00oOO0o , 15 , o0oO0 , i11Iiii , '' , '' , '' )
     else :
      Ii1I ( OOO00O , url + o00oOO0o , 14 , o0oO0 , i11Iiii , '' , '' , '' )
    elif o00oOO0o . endswith ( '.xml' ) :
     if browse :
      Ii1I ( OOO00O , url + o00oOO0o , 1 , o0oO0 , i11Iiii , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( o00 ) == True :
       if OOO00O in o000o0o00o0Oo :
        Ii1I ( OOO00O + ' (in use)' , url + o00oOO0o , 11 , o0oO0 , i11Iiii , '' , '' , '' , '' , 'download' )
       else :
        Ii1I ( OOO00O , url + o00oOO0o , 11 , o0oO0 , i11Iiii , '' , '' , '' , '' , 'download' )
      else :
       Ii1I ( OOO00O , url + o00oOO0o , 11 , o0oO0 , i11Iiii , '' , '' , '' , '' , 'download' )
       if 84 - 84: O0OOo * i1 / i1iIIII - O0
       if 30 - 30: iIii1I11I1II1 / i1iIIi1 - IiiIII111ii - II111iiii % IiiIIiiI11
def IIi1i11111 ( browse = False ) :
 ooOO00O00oo = 'http://community-links.googlecode.com/svn/trunk/'
 iiII1i1 = BeautifulSoup ( ii11iIi1I ( ooOO00O00oo ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 I1ii11iI = iiII1i1 ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for III1ii1iII in I1ii11iI :
  OOO00O = III1ii1iII ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   Ii1I ( OOO00O , ooOO00O00oo + OOO00O , 1 , o0oO0 , i11Iiii , '' , '' , '' , '' , 'download' )
  else :
   Ii1I ( OOO00O , ooOO00O00oo + OOO00O , 11 , o0oO0 , i11Iiii , '' , '' , '' , '' , 'download' )
   if 14 - 14: ii1IiI1i / oooOOOOO . ii1IiI1i . i1iIIII % i1 * i1iIIII
   if 16 - 16: ii1IiI1i . i1iIIi1 + i11iIiiIii
def OoOo00o ( url , data = None ) :
 print 'getsoup' , url , data
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = ii11iIi1I ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data' , data
   return data
   if 38 - 38: oooOOOOO * i1iII1I1i1i1 . IIIiiIIii
 elif data == None :
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    ooo0OO = xbmcvfs . copy ( url , os . path . join ( IiII , 'temp' , 'sorce_temp.txt' ) )
    if ooo0OO :
     data = open ( os . path . join ( IiII , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( IiII , 'temp' , 'sorce_temp.txt' ) )
    else :
     I1 ( "falha ao copiar do smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data' , data
     return data
  else :
   I1 ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 65 - 65: oO . iIii1I11I1II1 / O0 - oO
 if 21 - 21: OoOoOO00 * iIii1I11I1II1
def iiIIiIiIi ( url , icon , data = None ) :
 os . path . join ( iI1Ii11111iIi , 'resources' , 'fanart.gif' )
 iiII1i1 = OoOo00o ( url , data )
 if 91 - 91: oooOOOOO
 if isinstance ( iiII1i1 , BeautifulSOAP ) :
  if 15 - 15: II111iiii
  if len ( iiII1i1 ( 'search' ) ) > 0 :
   Ii = iiII1i1 ( 'search' )
   for ooo0O in Ii :
    oOoO0o00OO0 = ooo0O ( 'externallink' ) [ 0 ] . string
    OOO00O = ooo0O ( 'name' ) [ 0 ] . string
    try :
     OOO00O = oOo00Oo00O ( OOO00O )
    except : pass
    i1I1ii = ooo0O ( 'thumbnail' ) [ 0 ] . string
    if i1I1ii == None :
     i1I1ii = ''
    i1I1ii = oOo00Oo00O ( i1I1ii )
    try :
     if not ooo0O ( 'fanart' ) :
      if I11iIi1I . getSetting ( 'use_thumb' ) == "true" :
       oOOo0 = i1I1ii
      else :
       oOOo0 = i11Iiii
     else :
      oOOo0 = ooo0O ( 'fanart' ) [ 0 ] . string
     if oOOo0 == None :
      raise
    except :
     oOOo0 = i11Iiii
    try :
     Ii1I ( OOO00O . encode ( 'utf-8' ) , oOoO0o00OO0 . encode ( 'utf-8' ) , 55 , i1I1ii , oOOo0 , '' , '' , '' , None , 'source' )
    except :
     I1 ( 'There was a problem adding directory from getData(): ' + OOO00O . encode ( 'utf-8' , 'ignore' ) )
  else :
   I1 ( 'No Search: getItems' )
  if len ( iiII1i1 ( 'channels' ) ) > 0 :
   oo00O00oO = iiII1i1 ( 'channel' )
   for iIiIIIi in oo00O00oO :
    if 93 - 93: IiiIIiiI11
    oOoO0o00OO0 = ''
    i1IIIiiII1 = 0
    try :
     oOoO0o00OO0 = iIiIIIi ( 'externallink' ) [ 0 ] . string
     i1IIIiiII1 = len ( iIiIIIi ( 'externallink' ) )
    except : pass
    if i1IIIiiII1 > 1 : oOoO0o00OO0 = ''
    if 87 - 87: O0OOo * ooO00oOoo + i1iII1I1i1i1 / iIii1I11I1II1 / IiiIIiiI11
    OOO00O = iIiIIIi ( 'name' ) [ 0 ] . string
    i1I1ii = iIiIIIi ( 'thumbnail' ) [ 0 ] . string
    if i1I1ii == None :
     i1I1ii = ''
     if 37 - 37: IiiIIiiI11 - i1iIIi1 * O0OOo % i11iIiiIii - IiiIII111ii
    try :
     if not iIiIIIi ( 'fanart' ) :
      if I11iIi1I . getSetting ( 'use_thumb' ) == "true" :
       oOOo0 = i1I1ii
      else :
       oOOo0 = i11Iiii
     else :
      oOOo0 = iIiIIIi ( 'fanart' ) [ 0 ] . string
     if oOOo0 == None :
      raise
    except :
     oOOo0 = i11Iiii
     if 83 - 83: i1iIIII / OoOoOO00
    try :
     iII1i1I1II = iIiIIIi ( 'info' ) [ 0 ] . string
     if iII1i1I1II == None :
      raise
    except :
     iII1i1I1II = ''
     if 34 - 34: oooOOOOO
    try :
     I1I = iIiIIIi ( 'genre' ) [ 0 ] . string
     if I1I == None :
      raise
    except :
     I1I = ''
     if 57 - 57: O0OOo . i1iIIII . i1IIi
    try :
     i1IiIiiI = iIiIIIi ( 'date' ) [ 0 ] . string
     if i1IiIiiI == None :
      raise
    except :
     i1IiIiiI = ''
     if 42 - 42: i1iIIII + ooO00oOoo % O0
    try :
     credits = iIiIIIi ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 6 - 6: O0OOo
    try :
     if oOoO0o00OO0 == '' :
      Ii1I ( OOO00O . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , credits , True )
     else :
      if 68 - 68: ii1IiI1i - i1
      Ii1I ( OOO00O . encode ( 'utf-8' ) , oOoO0o00OO0 . encode ( 'utf-8' ) , 1 , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , None , 'source' )
    except :
     I1 ( 'Problema ao adicionar fonte(): ' + OOO00O . encode ( 'utf-8' , 'ignore' ) )
  else :
   I1 ( 'No Channels: getItems' )
   IIi ( iiII1i1 ( 'item' ) , i11Iiii )
 else :
  ooOOoooooo ( iiII1i1 )
  if 1 - 1: OOooo000oo0 / IIIiiIIii % IiiIIiiI11 * oooOOOOO . i11iIiiIii
  if 2 - 2: ooO00oOoo * i1iIIII - iIii1I11I1II1 + OoOoOO00 . O0OOo % IiiIIiiI11
def ooOOOoOooOoO ( url , icon , data = None ) :
 iIi11Ii1 = xbmc . Keyboard ( )
 iIi11Ii1 . setHeading ( "[COLOR lime][B]Brasil[COLOR yellow]Full [COLOR white]Pesquisa[/B][/COLOR]" )
 iIi11Ii1 . setDefault ( '' )
 iIi11Ii1 . doModal ( )
 if iIi11Ii1 . isConfirmed ( ) :
  o00oooO0Oo = iIi11Ii1 . getText ( )
  o00oooO0Oo = o00oooO0Oo . replace ( ' ' , '' ) . lower ( )
 else :
  xbmcgui . Dialog ( ) . ok ( '[COLOR lime][B]Brasil[COLOR yellow]Full[/B][/COLOR]' , '[COLOR white][B]Ue, vai pesquisar nada não?[/B][/COLOR]' )
  quit ( )
 i11Iiii = ''
 o0O0OOO0Ooo = False
 os . path . join ( iI1Ii11111iIi , 'resources' , 'fanart.gif' )
 iiII1i1 = OoOo00o ( url , data )
 if isinstance ( iiII1i1 , BeautifulSOAP ) :
  if len ( iiII1i1 ( 'link' ) ) > 0 :
   iiIiI = iiII1i1 ( 'item' )
   for I1OOO00O0O in iiIiI :
    ooo0O = I1OOO00O0O ( 'link' ) [ 0 ] . string
    iiII1i1 = OoOo00o ( ooo0O , data )
    iii = iiII1i1 ( 'item' )
    oOooOOOoOo = len ( iii )
    i1Iii1i1I = I11iIi1I . getSetting ( 'add_playlist' )
    OOoO00 = I11iIi1I . getSetting ( 'ask_playlist_items' )
    IiI111111IIII = I11iIi1I . getSetting ( 'use_thumb' )
    i1Ii = I11iIi1I . getSetting ( 'parentalblocked' )
    i1Ii = i1Ii == "true"
    for ii111iI1iIi1 in iii :
     try :
      OOO = False
      oo0OOo0 = False
      I11IiI = 'false'
      try :
       I11IiI = ii111iI1iIi1 ( 'parentalblock' ) [ 0 ] . string
      except :
       I1 ( 'parentalblock Error' )
       I11IiI = ''
      if I11IiI == 'true' and i1Ii : continue
      try :
       OOO00O = ii111iI1iIi1 ( 'title' ) [ 0 ] . string
       if OOO00O is None :
        OOO00O = 'unknown?'
       try :
        OOO00O = oOo00Oo00O ( OOO00O )
       except : pass
      except :
       I1 ( 'Name Error' )
       OOO00O = ''
      O0ooO0Oo00o = re . sub ( '\[.+?\]' , '' , OOO00O )
      if o00oooO0Oo in O0ooO0Oo00o . replace ( ' ' , '' ) . lower ( ) :
       try :
        if ii111iI1iIi1 ( 'epg' ) :
         if ii111iI1iIi1 . epg_url :
          I1 ( 'Get EPG Regex' )
          ooO0oOOooOo0 = ii111iI1iIi1 . epg_url . string
          i1I1ii11i1Iii = ii111iI1iIi1 . epg_regex . string
          I1IiiiiI = o0O ( ooO0oOOooOo0 , i1I1ii11i1Iii )
          if I1IiiiiI :
           OOO00O += ' - ' + I1IiiiiI
         elif ii111iI1iIi1 ( 'epg' ) [ 0 ] . string > 1 :
          OOO00O += IiIIii1iII1II ( ii111iI1iIi1 ( 'epg' ) [ 0 ] . string )
        else :
         pass
       except :
        I1 ( 'EPG Error' )
       url = [ ]
       if len ( ii111iI1iIi1 ( 'link' ) ) > 0 :
        if 48 - 48: II111iiii * oO . i1iIIII + O0OOo
        if 78 - 78: i11iIiiIii / IiiIIiiI11 - oO / i1iII1I1i1i1 + O0OOo
        for III1ii1iII in ii111iI1iIi1 ( 'link' ) :
         if not III1ii1iII . string == None :
          url . append ( III1ii1iII . string )
       elif len ( ii111iI1iIi1 ( 'utube' ) ) > 0 :
        for III1ii1iII in ii111iI1iIi1 ( 'utube' ) :
         if not III1ii1iII . string == None :
          if ' ' in III1ii1iII . string :
           oOoooo0O0Oo = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( III1ii1iII . string )
           oo0OOo0 = oOoooo0O0Oo
          elif len ( III1ii1iII . string ) == 11 :
           oOoooo0O0Oo = 'plugin://plugin.video.youtube/play/?video_id=' + III1ii1iII . string
          elif ( III1ii1iII . string . startswith ( 'PL' ) and not '&order=' in III1ii1iII . string ) or III1ii1iII . string . startswith ( 'UU' ) :
           oOoooo0O0Oo = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + III1ii1iII . string
          elif III1ii1iII . string . startswith ( 'PL' ) or III1ii1iII . string . startswith ( 'UU' ) :
           oOoooo0O0Oo = 'plugin://plugin.video.youtube/play/?playlist_id=' + III1ii1iII . string
          elif III1ii1iII . string . startswith ( 'UC' ) and len ( III1ii1iII . string ) > 12 :
           oOoooo0O0Oo = 'plugin://plugin.video.youtube/channel/' + III1ii1iII . string + '/'
           oo0OOo0 = oOoooo0O0Oo
          elif not III1ii1iII . string . startswith ( 'UC' ) and not ( III1ii1iII . string . startswith ( 'PL' ) ) :
           oOoooo0O0Oo = 'plugin://plugin.video.youtube/user/' + III1ii1iII . string + '/'
           oo0OOo0 = oOoooo0O0Oo
         url . append ( oOoooo0O0Oo )
       elif len ( ii111iI1iIi1 ( 'urlsolve' ) ) > 0 :
        for III1ii1iII in ii111iI1iIi1 ( 'urlsolve' ) :
         if not III1ii1iII . string == None :
          o00ooO = III1ii1iII . string + '&mode=19'
          url . append ( o00ooO )
       if len ( url ) < 1 :
        raise
       try :
        OOO = ii111iI1iIi1 ( 'externallink' ) [ 0 ] . string
       except : pass
       if 89 - 89: OOooo000oo0 * ii1IiI1i * IiiIII111ii + IiiIIiiI11 - i1iIIII
       if OOO :
        IIiiIiII1Ii = [ OOO ]
        OOO = True
       else :
        OOO = False
       try :
        oo0OOo0 = ii111iI1iIi1 ( 'jsonrpc' ) [ 0 ] . string
       except : pass
       if oo0OOo0 :
        IIiiIiII1Ii = [ oo0OOo0 ]
        oo0OOo0 = True
       else :
        oo0OOo0 = False
       try :
        i1I1ii = ii111iI1iIi1 ( 'thumbnail' ) [ 0 ] . string
        if i1I1ii == None :
         raise
        i1I1ii = oOo00Oo00O ( i1I1ii )
       except :
        i1I1ii = ''
       try :
        if not ii111iI1iIi1 ( 'fanart' ) :
         if I11iIi1I . getSetting ( 'use_thumb' ) == "true" :
          oOOo0 = i1I1ii
         else :
          oOOo0 = i11Iiii
        else :
         oOOo0 = ii111iI1iIi1 ( 'fanart' ) [ 0 ] . string
        if oOOo0 == None :
         raise
       except :
        oOOo0 = i11Iiii
       try :
        iII1i1I1II = ii111iI1iIi1 ( 'info' ) [ 0 ] . string
        if iII1i1I1II == None :
         raise
       except :
        iII1i1I1II = ''
       try :
        I1I = ii111iI1iIi1 ( 'genre' ) [ 0 ] . string
        if I1I == None :
         raise
       except :
        I1I = ''
       try :
        i1IiIiiI = ii111iI1iIi1 ( 'date' ) [ 0 ] . string
        if i1IiIiiI == None :
         raise
       except :
        i1IiIiiI = ''
       oo00oOO000oO0 = None
       if ii111iI1iIi1 ( 'regex' ) :
        try :
         iIIII11I1II = ii111iI1iIi1 ( 'regex' )
         oo00oOO000oO0 = Ii1IIiI1i ( iIIII11I1II )
        except :
         pass
       if len ( url ) > 1 :
        o0Oo00 = 0
        iIO0O0Oooo0o = [ ]
        oOOoo00O00o = True if '$$LSPlayOnlyOne$$' in url [ 0 ] else False
        if 98 - 98: i1iII1I1i1i1 + oooOOOOO + O0OOo % OoooooooOO
        for III1ii1iII in url :
         if i1Iii1i1I == "false" and not oOOoo00O00o :
          o0Oo00 += 1
          oooooo0O000o ( III1ii1iII , '%s) %s' % ( o0Oo00 , OOO00O . encode ( 'utf-8' , 'ignore' ) ) , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , True , iIO0O0Oooo0o , oo00oOO000oO0 , oOooOOOoOo )
         elif ( i1Iii1i1I == "true" and OOoO00 == 'true' ) or oOOoo00O00o :
          if oo00oOO000oO0 :
           iIO0O0Oooo0o . append ( III1ii1iII + '&regexs=' + oo00oOO000oO0 )
          elif any ( x in III1ii1iII for x in IiII1IiiIiI1 ) and III1ii1iII . startswith ( 'http' ) :
           iIO0O0Oooo0o . append ( III1ii1iII + '&mode=19' )
          else :
           iIO0O0Oooo0o . append ( III1ii1iII )
         else :
          iIO0O0Oooo0o . append ( III1ii1iII )
        if len ( iIO0O0Oooo0o ) > 1 :
         oooooo0O000o ( '' , OOO00O . encode ( 'utf-8' ) , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , True , iIO0O0Oooo0o , oo00oOO000oO0 , oOooOOOoOo )
       else :
        if o0O0OOO0Ooo :
         return OOO00O , url [ 0 ] , oo00oOO000oO0
        if OOO :
         if not oo00oOO000oO0 == None :
          Ii1I ( OOO00O . encode ( 'utf-8' ) , IIiiIiII1Ii [ 0 ] . encode ( 'utf-8' ) , 1 , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , None , '!!update' , oo00oOO000oO0 , url [ 0 ] . encode ( 'utf-8' ) )
         else :
          Ii1I ( OOO00O . encode ( 'utf-8' ) , IIiiIiII1Ii [ 0 ] . encode ( 'utf-8' ) , 1 , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , None , 'source' , None , None )
        elif oo0OOo0 :
         Ii1I ( OOO00O . encode ( 'utf-8' ) , IIiiIiII1Ii [ 0 ] , 53 , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , None , 'source' )
        else :
         oooooo0O000o ( url [ 0 ] , OOO00O . encode ( 'utf-8' , 'ignore' ) , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , True , None , oo00oOO000oO0 , oOooOOOoOo )
     except : pass
     if 64 - 64: OoOoOO00 . IIIiiIIii - IiiIII111ii / OoooooooOO
def ooOOoooooo ( data ) :
 O0O0ooOOO = data . rstrip ( )
 oOOo0O00o = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)' ) . findall ( O0O0ooOOO )
 oOooOOOoOo = len ( oOOo0O00o )
 print 'total m3u links' , oOooOOOoOo
 for iIiIi11 , OOOiiiiI , oooOo0OOOoo0 in oOOo0O00o :
  if 'tvg-logo' in iIiIi11 :
   i1I1ii = OOoO ( iIiIi11 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if i1I1ii :
    if i1I1ii . startswith ( 'http' ) :
     i1I1ii = i1I1ii
     if 89 - 89: IIIiiIIii + i1 * i1iIIII * oO
    elif not I11iIi1I . getSetting ( 'logo-folderPath' ) == "" :
     iiIiI1i1 = I11iIi1I . getSetting ( 'logo-folderPath' )
     i1I1ii = iiIiI1i1 + i1I1ii
     if 69 - 69: i1iIIi1
    else :
     i1I1ii = i1I1ii
     if 40 - 40: IiiIII111ii + OoooooooOO % IIIiiIIii - iIii1I11I1II1 . OoOoOO00
     if 48 - 48: IIIiiIIii - O0OOo / OoooooooOO
  else :
   i1I1ii = ''
  if 'type' in iIiIi11 :
   OO0O0 = OOoO ( iIiIi11 , 'type=[\'"](.*?)[\'"]' )
   if OO0O0 == 'yt-dl' :
    oooOo0OOOoo0 = oooOo0OOOoo0 + "&mode=18"
   elif OO0O0 == 'regex' :
    ooOO00O00oo = oooOo0OOOoo0 . split ( '&regexs=' )
    oo00oOO000oO0 = Ii1IIiI1i ( OoOo00o ( '' , data = ooOO00O00oo [ 1 ] ) )
    if 30 - 30: i1iII1I1i1i1 + ooO00oOoo * i1iIIII % i11iIiiIii % ii1IiI1i
    oooooo0O000o ( ooOO00O00oo [ 0 ] , OOOiiiiI , i1I1ii , '' , '' , '' , '' , '' , None , oo00oOO000oO0 , oOooOOOoOo )
    continue
  oooooo0O000o ( oooOo0OOOoo0 , OOOiiiiI , i1I1ii , '' , '' , '' , '' , '' , None , '' , oOooOOOoOo )
  if 97 - 97: ooO00oOoo % ooO00oOoo % O0OOo / IiiIIiiI11 - iIii1I11I1II1
 xbmc . executebuiltin ( "Container.SetViewMode(50)" )
 if 69 - 69: IiiIII111ii
def ii1I1 ( name , url , fanart ) :
 iiII1i1 = OoOo00o ( url )
 OooooOOoo0 = iiII1i1 . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 iii = OooooOOoo0 ( 'item' )
 try :
  oOOo0 = OooooOOoo0 ( 'fanart' ) [ 0 ] . string
  if oOOo0 == None :
   raise
 except :
  oOOo0 = fanart
 for iIiIIIi in OooooOOoo0 ( 'subchannel' ) :
  name = iIiIIIi ( 'name' ) [ 0 ] . string
  try :
   i1I1ii = iIiIIIi ( 'thumbnail' ) [ 0 ] . string
   if i1I1ii == None :
    raise
  except :
   i1I1ii = ''
  try :
   if not iIiIIIi ( 'fanart' ) :
    if I11iIi1I . getSetting ( 'use_thumb' ) == "true" :
     oOOo0 = i1I1ii
   else :
    oOOo0 = iIiIIIi ( 'fanart' ) [ 0 ] . string
   if oOOo0 == None :
    raise
  except :
   pass
  try :
   iII1i1I1II = iIiIIIi ( 'info' ) [ 0 ] . string
   if iII1i1I1II == None :
    raise
  except :
   iII1i1I1II = ''
   if 35 - 35: i1iIIII % i1iII1I1i1i1 - O0OOo
  try :
   I1I = iIiIIIi ( 'genre' ) [ 0 ] . string
   if I1I == None :
    raise
  except :
   I1I = ''
   if 20 - 20: i1IIi - i1iIIi1
  try :
   i1IiIiiI = iIiIIIi ( 'date' ) [ 0 ] . string
   if i1IiIiiI == None :
    raise
  except :
   i1IiIiiI = ''
   if 30 - 30: i1iIIII / OoOoOO00
  try :
   credits = iIiIIIi ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 35 - 35: II111iiii % i1iII1I1i1i1 . i1iIIi1 + i1iIIi1 % II111iiii % II111iiii
  try :
   Ii1I ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , i1I1ii , oOOo0 , iII1i1I1II , I1I , credits , i1IiIiiI )
  except :
   I1 ( 'Problema ao adicionar diretório - ' + name . encode ( 'utf-8' , 'ignore' ) )
 IIi ( iii , oOOo0 )
 if 72 - 72: II111iiii + i1IIi + IIIiiIIii
 if 94 - 94: O0OOo . i1IIi - IIIiiIIii % O0 - i1
def ooO0O00Oo0o ( name , url , fanart ) :
 iiII1i1 = OoOo00o ( url )
 OooooOOoo0 = iiII1i1 . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 iii = OooooOOoo0 ( 'subitem' )
 IIi ( iii , fanart )
 if 65 - 65: ooO00oOoo . i1iIIII - IiiIII111ii * oooOOOOO / IiiIII111ii / i1iIIi1
def i111iIi1i1II1 ( name , url , iconimage , fanart ) :
 oooO = [ ] ; i1I1i111Ii = [ ] ; ooo = 0
 i1i1iI1iiiI = Ooo0oOooo0 ( url , 'sublink:' , '#' )
 for oOOOoo00 in i1i1iI1iiiI :
  iiIiIIIiiI = oOOOoo00 . replace ( 'sublink:' , '' ) . replace ( '#' , '' )
  if len ( iiIiIIIiiI ) > 10 :
   ooo = ooo + 1 ; oooO . append ( name + ' Source [' + str ( ooo ) + ']' ) ; i1I1i111Ii . append ( iiIiIIIiiI )
   if 12 - 12: O0 - IIIiiIIii
 if ooo == 1 :
  try :
   oOoO00O0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; oOoO00O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
   OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1i111Ii [ 0 ] , listitem = oOoO00O0 )
   xbmc . Player ( ) . play ( Ii1iI111II1I1 ( i1I1i111Ii [ 0 ] ) , oOoO00O0 )
  except :
   pass
 else :
  oOOOOoOO0o = xbmcgui . Dialog ( )
  i1II1 = oOOOOoOO0o . select ( '[COLOR green][B]Brasil [/B][/COLOR][COLOR yellow][B]Full[/B][/COLOR] Selecione uma opção:' , oooO )
  if i1II1 >= 0 :
   i11i1 = name
   IiiiiI1i1Iii = str ( i1I1i111Ii [ i1II1 ] )
   try :
    oOoO00O0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; oOoO00O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
    OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiiI1i1Iii , listitem = oOoO00O0 )
    xbmc . Player ( ) . play ( Ii1iI111II1I1 ( IiiiiI1i1Iii ) , oOoO00O0 )
   except :
    pass
    if 87 - 87: IIIiiIIii
    if 29 - 29: OoOoOO00 % i1iII1I1i1i1 - OoOoOO00 / i1iII1I1i1i1 . i1IIi
def i11III1111iIi ( ) :
 I1i111I = 'Nome do canal ou filme'
 Ooo = ''
 iIi11Ii1 = xbmc . Keyboard ( Ooo , I1i111I )
 iIi11Ii1 . doModal ( )
 if iIi11Ii1 . isConfirmed ( ) :
  Ooo = iIi11Ii1 . getText ( ) . replace ( '\n' , '' ) . strip ( )
  if len ( Ooo ) == 0 :
   xbmcgui . Dialog ( ) . ok ( 'RobinHood' , 'Nothing Entered' )
   return
   if 65 - 65: O0 * OoooooooOO % i1iII1I1i1i1 / oooOOOOO - oO / i1iIIII
 Ooo = Ooo . lower ( )
 oooO = [ ]
 oooO . append ( _Edit . MainBase )
 oo0o00o0OoOo = 0
 OOOOoOOo0O0 = 1
 oOooo0 = 0
 ooO = 0
 o0o00OOo0 = xbmcgui . DialogProgress ( )
 o0o00OOo0 . create ( 'BrasilFull Procurando Espere' , ' ' )
 if 17 - 17: IiiIII111ii + O0OOo - i11iIiiIii . IiiIII111ii * i1iII1I1i1i1
 while OOOOoOOo0O0 <> oOooo0 :
  oo0oOOO0OOOo = oooO [ oOooo0 ] . strip ( )
  print 'read this one from file list (' + str ( oOooo0 ) + ')'
  oOooo0 = oOooo0 + 1
  if 56 - 56: IIIiiIIii
  I1OooooO0oOOOO = ''
  try :
   I1OooooO0oOOOO = net . http_GET ( oo0oOOO0OOOo ) . content
   I1OooooO0oOOOO = I1OooooO0oOOOO . encode ( 'ascii' , 'ignore' ) . decode ( 'ascii' )
  except :
   pass
   if 100 - 100: IiiIIiiI11 % i1iII1I1i1i1
  if len ( I1OooooO0oOOOO ) < 10 :
   I1OooooO0oOOOO = ''
   oo0o00o0OoOo = oo0o00o0OoOo + 1
   print '*** PASSED ****' + oo0oOOO0OOOo + '  ************* Total Passed Urls: ' + str ( oo0o00o0OoOo )
   time . sleep ( .5 )
   if 86 - 86: OOooo000oo0 . O0 - OoooooooOO . i1 + oO
  OOo = int ( ( oOooo0 / 300 ) * 100 )
  IIii11Ii1i1I = '     Pages Read: ' + str ( oOooo0 ) + '        Matches Found: ' + str ( ooO )
  o0o00OOo0 . update ( OOo , "" , IIii11Ii1i1I , "" )
  if 76 - 76: O0 + i1IIi . OOooo000oo0 * OoOoOO00 * oO
  if o0o00OOo0 . iscanceled ( ) :
   return
   if 14 - 14: IIIiiIIii % O0 * IiiIIiiI11 + oO + OOooo000oo0 * oO
  if len ( I1OooooO0oOOOO ) > 10 :
   iII1I1IiI11ii = Ooo0oOooo0 ( I1OooooO0oOOOO , '<channel>' , '</channel>' )
   for oOOOoo00 in iII1I1IiI11ii :
    iiIiIIIiiI = OooooOoooO ( oOOOoo00 , '<externallink>' , '</externallink>' )
    if len ( iiIiIIIiiI ) > 5 :
     OOOOoOOo0O0 = OOOOoOOo0O0 + 1
     oooO . append ( iiIiIIIiiI )
     if 56 - 56: OOooo000oo0 . ooO00oOoo . OoOoOO00
   ii111I = Ooo0oOooo0 ( I1OooooO0oOOOO , '<item>' , '</item>' )
   for oOOOoo00 in ii111I :
    iiIiIIIiiI = OooooOoooO ( oOOOoo00 , '<link>' , '</link>' )
    OOO00O = OooooOoooO ( oOOOoo00 , '<title>' , '</title>' )
    iiI = '  ' + OOO00O . lower ( ) + '  '
    if len ( iiIiIIIiiI ) > 5 and iiI . find ( Ooo ) > 0 :
     ooO = ooO + 1
     i11Iiii = ''
     i1I1ii = OooooOoooO ( oOOOoo00 , '<thumbnail>' , '</thumbnail>' )
     i11Iiii = OooooOoooO ( oOOOoo00 , '<fanart>' , '</fanart>' )
     if len ( i11Iiii ) < 5 :
      i11Iiii = o0oO0
     if iiIiIIIiiI . find ( 'sublink' ) > 0 :
      Ii1I ( OOO00O , iiIiIIIiiI , 30 , i1I1ii , i11Iiii , '' , '' , '' , '' )
     else :
      oooooo0O000o ( str ( iiIiIIIiiI ) , OOO00O , i1I1ii , i11Iiii , '' , '' , '' , True , None , '' , 1 )
      if 7 - 7: ii1IiI1i + II111iiii . i1IIi
      if 63 - 63: iIii1I11I1II1 / IiiIII111ii / O0OOo / IiiIIiiI11
 o0o00OOo0 . close ( )
 xbmc . executebuiltin ( "Container.SetViewMode(50)" )
 if 33 - 33: oooOOOOO % iIii1I11I1II1 * OoOoOO00
def o00o0 ( data , Searchkey ) :
 O0O0ooOOO = data . rstrip ( )
 oOOo0O00o = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)' ) . findall ( O0O0ooOOO )
 oOooOOOoOo = len ( oOOo0O00o )
 print 'total m3u links' , oOooOOOoOo
 for iIiIi11 , OOOiiiiI , oooOo0OOOoo0 in oOOo0O00o :
  if 'tvg-logo' in iIiIi11 :
   i1I1ii = OOoO ( iIiIi11 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if i1I1ii :
    if i1I1ii . startswith ( 'http' ) :
     i1I1ii = i1I1ii
     if 50 - 50: OOooo000oo0 / OOooo000oo0 % ooO00oOoo . ooO00oOoo
    elif not I11iIi1I . getSetting ( 'logo-folderPath' ) == "" :
     iiIiI1i1 = I11iIi1I . getSetting ( 'logo-folderPath' )
     i1I1ii = iiIiI1i1 + i1I1ii
     if 55 - 55: i1iIIi1 - i1iIIII + II111iiii + IiiIIiiI11 % oO
    else :
     i1I1ii = i1I1ii
     if 41 - 41: i1IIi - i1iIIII - oO
  else :
   i1I1ii = ''
  if 'type' in iIiIi11 :
   OO0O0 = OOoO ( iIiIi11 , 'type=[\'"](.*?)[\'"]' )
   if OO0O0 == 'yt-dl' :
    oooOo0OOOoo0 = oooOo0OOOoo0 + "&mode=18"
   elif OO0O0 == 'regex' :
    ooOO00O00oo = oooOo0OOOoo0 . split ( '&regexs=' )
    oo00oOO000oO0 = Ii1IIiI1i ( OoOo00o ( '' , data = ooOO00O00oo [ 1 ] ) )
    if 8 - 8: i1 + IiiIII111ii - IIIiiIIii % OOooo000oo0 % IIIiiIIii * O0OOo
    oooooo0O000o ( ooOO00O00oo [ 0 ] , OOOiiiiI , i1I1ii , '' , '' , '' , '' , '' , None , oo00oOO000oO0 , oOooOOOoOo )
    continue
  oooooo0O000o ( oooOo0OOOoo0 , OOOiiiiI , i1I1ii , '' , '' , '' , '' , '' , None , '' , oOooOOOoOo )
  if 9 - 9: OOooo000oo0 - i11iIiiIii - i1iII1I1i1i1 * oO + i1iIIi1
def iIIII ( text , pattern ) :
 iIIIiiI1i1i = ""
 try :
  iIII = re . findall ( pattern , text , flags = re . DOTALL )
  iIIIiiI1i1i = iIII [ 0 ]
 except :
  iIIIiiI1i1i = ""
  if 70 - 70: IiiIIiiI11 / iIii1I11I1II1
 return iIIIiiI1i1i
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / ooO00oOoo
def Ooo0oOooo0 ( text , start_with , end_with ) :
 ooOOoO = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return ooOOoO
 if 20 - 20: i1iIIII + oO / O0 % iIii1I11I1II1
def OooooOoooO ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : ooOOoO = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : ooOOoO = ''
 else :
  try : ooOOoO = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : ooOOoO = ''
 return ooOOoO
 if 88 - 88: ii1IiI1i / II111iiii
def IIi ( items , fanart , dontLink = False ) :
 oOooOOOoOo = len ( items )
 I1 ( 'Total Items: %s' % oOooOOOoOo )
 i1Iii1i1I = I11iIi1I . getSetting ( 'add_playlist' )
 OOoO00 = I11iIi1I . getSetting ( 'ask_playlist_items' )
 IiI111111IIII = I11iIi1I . getSetting ( 'use_thumb' )
 i1Ii = I11iIi1I . getSetting ( 'parentalblocked' )
 i1Ii = i1Ii == "true"
 for ii111iI1iIi1 in items :
  OOO = False
  oo0OOo0 = False
  if 87 - 87: ooO00oOoo - ooO00oOoo - IiiIIiiI11 + O0OOo
  I11IiI = 'false'
  try :
   I11IiI = ii111iI1iIi1 ( 'parentalblock' ) [ 0 ] . string
  except :
   I1 ( 'parentalblock Error' )
   I11IiI = ''
  if I11IiI == 'true' and i1Ii : continue
  if 82 - 82: O0OOo / iIii1I11I1II1 . OoOoOO00 . i1iII1I1i1i1 / IIIiiIIii
  try :
   OOO00O = ii111iI1iIi1 ( 'title' ) [ 0 ] . string
   if OOO00O is None :
    OOO00O = 'unknown?'
  except :
   I1 ( 'Name Error' )
   OOO00O = ''
   if 42 - 42: OOooo000oo0
   if 19 - 19: O0OOo % ooO00oOoo * iIii1I11I1II1 + OoOoOO00
  try :
   if ii111iI1iIi1 ( 'epg' ) :
    if ii111iI1iIi1 . epg_url :
     I1 ( 'Get EPG Regex' )
     ooO0oOOooOo0 = ii111iI1iIi1 . epg_url . string
     i1I1ii11i1Iii = ii111iI1iIi1 . epg_regex . string
     I1IiiiiI = o0O ( ooO0oOOooOo0 , i1I1ii11i1Iii )
     if I1IiiiiI :
      OOO00O += ' - ' + I1IiiiiI
    elif ii111iI1iIi1 ( 'epg' ) [ 0 ] . string > 1 :
     OOO00O += IiIIii1iII1II ( ii111iI1iIi1 ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   I1 ( 'EPG Error' )
  try :
   ooOO00O00oo = [ ]
   if len ( ii111iI1iIi1 ( 'link' ) ) > 0 :
    if 46 - 46: OOooo000oo0
    for III1ii1iII in ii111iI1iIi1 ( 'link' ) :
     if not III1ii1iII . string == None :
      ooOO00O00oo . append ( III1ii1iII . string )
      if 1 - 1: IiiIIiiI11
   elif len ( ii111iI1iIi1 ( 'sportsdevil' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'sportsdevil' ) :
     if not III1ii1iII . string == None :
      O0O0Ooo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + III1ii1iII . string
      oOoO0 = ii111iI1iIi1 ( 'referer' ) [ 0 ] . string
      if oOoO0 :
       O0O0Ooo = O0O0Ooo + '%26referer=' + oOoO0
      ooOO00O00oo . append ( O0O0Ooo )
   elif len ( ii111iI1iIi1 ( 'p2p' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'p2p' ) :
     if not III1ii1iII . string == None :
      if 'sop://' in III1ii1iII :
       Oo0 = 'plugin://plugin.video.p2p-streams/?url=' + III1ii1iII . string + '&amp;mode=2&amp;' + 'name=' + OOO00O
       ooOO00O00oo . append ( Oo0 )
      else :
       oo0O0o00o0O = 'plugin://plugin.video.p2p-streams/?url=' + III1ii1iII . string + '&amp;mode=1&amp;' + 'name=' + OOO00O
       ooOO00O00oo . append ( oo0O0o00o0O )
   elif len ( ii111iI1iIi1 ( 'vaughn' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'vaughn' ) :
     if not III1ii1iII . string == None :
      I11i1II = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + III1ii1iII . string
      ooOO00O00oo . append ( I11i1II )
   elif len ( ii111iI1iIi1 ( 'ilive' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'ilive' ) :
     if not III1ii1iII . string == None :
      if not 'http' in III1ii1iII . string :
       OooiiIi1i = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + III1ii1iII . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       OooiiIi1i = 'plugin://plugin.video.tbh.ilive/?url=' + III1ii1iII . string + '&amp;link=99&amp;mode=iLivePlay'
       if 27 - 27: i1iII1I1i1i1 * i1iIIi1 . IiiIII111ii % oooOOOOO * oooOOOOO . i1IIi
   elif len ( ii111iI1iIi1 ( 'trailer' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'trailer' ) :
     if not III1ii1iII . string == None :
      O0OOoOOO0oO = + III1ii1iII . string
      ooOO00O00oo . append ( O0OOoOOO0oO )
      if 28 - 28: i1iIIi1 + i11iIiiIii / i1iIIII % ii1IiI1i % OOooo000oo0 - O0
   elif len ( ii111iI1iIi1 ( 'yt-dl' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'yt-dl' ) :
     if not III1ii1iII . string == None :
      ooo0OOO = III1ii1iII . string + '&mode=18'
      ooOO00O00oo . append ( ooo0OOO )
      if 49 - 49: i11iIiiIii % oO . ii1IiI1i
   elif len ( ii111iI1iIi1 ( 'putube' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'putube' ) :
     if not III1ii1iII . string == None :
      Ii1i1iI = 'plugin://plugin.video.youtube/playlist/' + III1ii1iII . string + '/'
      plugintools . add_item (
 title = "-" + OOO00O + "" ,
 url = Ii1i1iI ,
 thumbnail = o0oO0 ,
 folder = True )
      ooOO00O00oo . append ( Ii1i1iI )
      if 16 - 16: i1iII1I1i1i1 / OOooo000oo0 / OoooooooOO * OoOoOO00 + i1IIi % i1iII1I1i1i1
   elif len ( ii111iI1iIi1 ( 'utube' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'utube' ) :
     if not III1ii1iII . string == None :
      if ' ' in III1ii1iII . string :
       oOoooo0O0Oo = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( III1ii1iII . string )
       oo0OOo0 = oOoooo0O0Oo
      elif len ( III1ii1iII . string ) == 11 :
       oOoooo0O0Oo = 'plugin://plugin.video.youtube/play/?video_id=' + III1ii1iII . string
      elif ( III1ii1iII . string . startswith ( 'PL' ) and not '&order=' in III1ii1iII . string ) or III1ii1iII . string . startswith ( 'UU' ) :
       oOoooo0O0Oo = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + III1ii1iII . string
      elif III1ii1iII . string . startswith ( 'PL' ) or III1ii1iII . string . startswith ( 'UU' ) :
       oOoooo0O0Oo = 'plugin://plugin.video.youtube/play/?playlist_id=' + III1ii1iII . string
      elif III1ii1iII . string . startswith ( 'UC' ) and len ( III1ii1iII . string ) > 12 :
       oOoooo0O0Oo = 'plugin://plugin.video.youtube/channel/' + III1ii1iII . string + '/'
       oo0OOo0 = oOoooo0O0Oo
      elif not III1ii1iII . string . startswith ( 'UC' ) and not ( III1ii1iII . string . startswith ( 'PL' ) ) :
       oOoooo0O0Oo = 'plugin://plugin.video.youtube/user/' + III1ii1iII . string + '/'
       oo0OOo0 = oOoooo0O0Oo
     ooOO00O00oo . append ( oOoooo0O0Oo )
     if 71 - 71: ii1IiI1i
   elif len ( ii111iI1iIi1 ( 'gdrive' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'gdrive' ) :
     if not III1ii1iII . string == None :
      ii111IiiI1 = 'plugin://plugin.video.gdrive?mode=streamURL&amp;url=https://docs.google.com/file/d/' + III1ii1iII . string
      ooOO00O00oo . append ( ii111IiiI1 )
      if 11 - 11: iIii1I11I1II1 * oO
   elif len ( ii111iI1iIi1 ( 'drive' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'drive' ) :
     if not III1ii1iII . string == None :
      ii111IiiI1 = 'plugin://plugin.video.gdrive?mode=streamURL&amp;url=https://drive.google.com/open?id=' + III1ii1iII . string
      ooOO00O00oo . append ( drive )
      if 76 - 76: i1iIIi1
   elif len ( ii111iI1iIi1 ( 'imdb' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'imdb' ) :
     if not III1ii1iII . string == None :
      if I11iIi1I . getSetting ( 'genesisorpulsar' ) == '0' :
       II = 'plugin://plugin.video.genesis/?action=play&imdb=' + III1ii1iII . string
      else :
       II = 'plugin://plugin.video.quasar/movie/tt' + III1ii1iII . string + '/play'
      ooOO00O00oo . append ( II )
      if 45 - 45: OoooooooOO - i1iII1I1i1i1 + O0 * oO . ooO00oOoo
   elif len ( ii111iI1iIi1 ( 'f4m' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'f4m' ) :
     if not III1ii1iII . string == None :
      if 39 - 39: iIii1I11I1II1 / O0 / O0OOo - oO - IiiIIiiI11 % i1iII1I1i1i1
      if '.f4m' in III1ii1iII . string :
       I1ii11Ii = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( III1ii1iII . string )
      elif '.m3u8' in III1ii1iII . string :
       I1ii11Ii = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( III1ii1iII . string ) + '&amp;streamtype=HLS'
      elif '.ts' in III1ii1iII . string :
       I1ii11Ii = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( III1ii1iII . string ) + '&amp;streamtype=TSDOWNLOADER&amp;name=' + OOO00O
      else :
       I1ii11Ii = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( III1ii1iII . string ) + '&amp;streamtype=SIMPLE'
    ooOO00O00oo . append ( I1ii11Ii )
    if 50 - 50: i1iIIi1 - IiiIII111ii * oooOOOOO . ooO00oOoo
   elif len ( ii111iI1iIi1 ( 'ftv' ) ) > 0 :
    for III1ii1iII in ii111iI1iIi1 ( 'ftv' ) :
     if not III1ii1iII . string == None :
      I11iiiii1II = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( OOO00O ) + '&url=' + III1ii1iII . string + '&mode=125&ch_fanart=na'
     ooOO00O00oo . append ( I11iiiii1II )
   if len ( ooOO00O00oo ) < 1 :
    raise
  except :
   I1 ( 'Error <link> element, Passing:' + OOO00O . encode ( 'utf-8' , 'ignore' ) )
   continue
   if 51 - 51: O0 % O0OOo - II111iiii
  OOO = False
  if 31 - 31: IiiIIiiI11 / OOooo000oo0 - IiiIIiiI11 - i1iII1I1i1i1
  try :
   OOO = ii111iI1iIi1 ( 'externallink' ) [ 0 ] . string
  except : pass
  if 7 - 7: IiiIIiiI11 % O0 . ii1IiI1i + OoOoOO00 - i1iIIII
  if OOO :
   IIiiIiII1Ii = [ OOO ]
   OOO = True
  else :
   OOO = False
  try :
   oo0OOo0 = ii111iI1iIi1 ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if oo0OOo0 :
   IIiiIiII1Ii = [ oo0OOo0 ]
   oo0OOo0 = True
  else :
   oo0OOo0 = False
  try :
   i1I1ii = ii111iI1iIi1 ( 'thumbnail' ) [ 0 ] . string
   if i1I1ii == None :
    raise
  except :
   i1I1ii = ''
  try :
   if not ii111iI1iIi1 ( 'fanart' ) :
    if I11iIi1I . getSetting ( 'use_thumb' ) == "true" :
     oOOo0 = i1I1ii
    else :
     oOOo0 = fanart
   else :
    oOOo0 = ii111iI1iIi1 ( 'fanart' ) [ 0 ] . string
   if oOOo0 == None :
    raise
  except :
   oOOo0 = fanart
  try :
   iII1i1I1II = ii111iI1iIi1 ( 'info' ) [ 0 ] . string
   if iII1i1I1II == None :
    raise
  except :
   iII1i1I1II = ''
   if 75 - 75: i1iIIII
  try :
   I1I = ii111iI1iIi1 ( 'genre' ) [ 0 ] . string
   if I1I == None :
    raise
  except :
   I1I = ''
   if 71 - 71: i1iIIi1
  try :
   i1IiIiiI = ii111iI1iIi1 ( 'date' ) [ 0 ] . string
   if i1IiIiiI == None :
    raise
  except :
   i1IiIiiI = ''
   if 53 - 53: OoooooooOO % oO . oooOOOOO / i11iIiiIii % IiiIIiiI11
  oo00oOO000oO0 = None
  if ii111iI1iIi1 ( 'regex' ) :
   try :
    iIIII11I1II = ii111iI1iIi1 ( 'regex' )
    oo00oOO000oO0 = Ii1IIiI1i ( iIIII11I1II )
   except :
    pass
    if 28 - 28: i1iIIII
  try :
   if len ( ooOO00O00oo ) > 1 :
    if 58 - 58: ii1IiI1i
    o0Oo00 = 0
    iIO0O0Oooo0o = [ ]
    for III1ii1iII in ooOO00O00oo :
     if I11iIi1I . getSetting ( 'ask_playlist_items' ) == 'true' :
      if oo00oOO000oO0 :
       iIO0O0Oooo0o . append ( III1ii1iII + '&regexs=' + oo00oOO000oO0 )
      elif any ( x in III1ii1iII for x in IiII1IiiIiI1 ) and III1ii1iII . startswith ( 'http' ) :
       iIO0O0Oooo0o . append ( III1ii1iII + '&mode=19' )
     else :
      iIO0O0Oooo0o . append ( III1ii1iII )
    for III1ii1iII in ooOO00O00oo :
     if i1Iii1i1I == "false" and not ignorelistsetting :
      o0Oo00 += 1
      oooooo0O000o ( III1ii1iII , '%s) %s' % ( o0Oo00 , OOO00O . encode ( 'utf-8' , 'ignore' ) ) , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , True , iIO0O0Oooo0o , oo00oOO000oO0 , oOooOOOoOo )
     elif ( i1Iii1i1I == "true" and OOoO00 == 'true' ) or ignorelistsetting :
      if oo00oOO000oO0 :
       iIO0O0Oooo0o . append ( III1ii1iII + '&regexs=' + oo00oOO000oO0 )
      elif any ( x in III1ii1iII for x in IiII1IiiIiI1 ) and III1ii1iII . startswith ( 'http' ) :
       iIO0O0Oooo0o . append ( III1ii1iII + '&mode=19' )
      else :
       iIO0O0Oooo0o . append ( III1ii1iII )
     else :
      iIO0O0Oooo0o . append ( III1ii1iII )
    else :
     oooooo0O000o ( '' , OOO00O . encode ( 'utf-8' , 'ignore' ) , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , True , iIO0O0Oooo0o , oo00oOO000oO0 , oOooOOOoOo )
   else :
    if OOO :
     Ii1I ( OOO00O . encode ( 'utf-8' ) , IIiiIiII1Ii [ 0 ] . encode ( 'utf-8' ) , 1 , i1I1ii , fanart , iII1i1I1II , I1I , i1IiIiiI , None , 'source' )
    elif oo0OOo0 :
     Ii1I ( OOO00O . encode ( 'utf-8' ) , IIiiIiII1Ii [ 0 ] , 53 , i1I1ii , fanart , iII1i1I1II , I1I , i1IiIiiI , None , 'source' )
    elif ooOO00O00oo [ 0 ] . find ( 'sublink' ) > 0 :
     Ii1I ( OOO00O . encode ( 'utf-8' ) , ooOO00O00oo [ 0 ] , 30 , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , None )
    else :
     oooooo0O000o ( ooOO00O00oo [ 0 ] , OOO00O . encode ( 'utf-8' , 'ignore' ) , i1I1ii , oOOo0 , iII1i1I1II , I1I , i1IiIiiI , True , None , oo00oOO000oO0 , oOooOOOoOo )
     if 37 - 37: OOooo000oo0 - iIii1I11I1II1 / ooO00oOoo
  except :
   I1 ( 'Problema ao adicionar item - ' + OOO00O . encode ( 'utf-8' , 'ignore' ) )
 print 'FINISH GET ITEMS *****'
 if 73 - 73: i11iIiiIii - oooOOOOO
def Ii1IIiI1i ( reg_item ) :
 try :
  oo00oOO000oO0 = { }
  for III1ii1iII in reg_item :
   oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] = { }
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'expre' ] = III1ii1iII ( 'expres' ) [ 0 ] . string
    if not oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'expre' ] :
     oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'expre' ] = ''
   except :
    I1 ( "Regex: -- No Referer --" )
   oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'page' ] = III1ii1iII ( 'page' ) [ 0 ] . string
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'refer' ] = III1ii1iII ( 'referer' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No Referer --" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'connection' ] = III1ii1iII ( 'connection' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No connection --" )
    if 25 - 25: OoooooooOO + oooOOOOO * ooO00oOoo
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = III1ii1iII ( 'notplayable' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No notplayable --" )
    if 92 - 92: OoOoOO00 + i1iIIII + O0 / IIIiiIIii + IiiIII111ii
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = III1ii1iII ( 'noredirect' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No noredirect --" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'origin' ] = III1ii1iII ( 'origin' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No origin --" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = III1ii1iII ( 'includeheaders' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No includeheaders --" )
    if 18 - 18: i1iIIi1 * ii1IiI1i . IiiIIiiI11 / ooO00oOoo / i11iIiiIii
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = III1ii1iII ( 'x-req' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No x-req --" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = III1ii1iII ( 'x-forward' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No x-forward --" )
    if 21 - 21: O0OOo / ooO00oOoo + oO + OoooooooOO
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'agent' ] = III1ii1iII ( 'agent' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- No User Agent --" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'post' ] = III1ii1iII ( 'post' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- Not a post" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = III1ii1iII ( 'rawpost' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- Not a rawpost" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = III1ii1iII ( 'htmlunescape' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- Not a htmlunescape" )
    if 91 - 91: i11iIiiIii / i1IIi + IiiIIiiI11 + i1iIIi1 * i11iIiiIii
    if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + i1iIIII * IiiIII111ii . oooOOOOO
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = III1ii1iII ( 'readcookieonly' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- Not a readCookieOnly" )
    if 52 - 52: i1iIIi1 + O0 . IiiIIiiI11 . ooO00oOoo . i1
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = III1ii1iII ( 'cookiejar' ) [ 0 ] . string
    if not oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    I1 ( "Regex: -- Not a cookieJar" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = III1ii1iII ( 'setcookie' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- Not a setcookie" )
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = III1ii1iII ( 'appendcookie' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- Not a appendcookie" )
    if 97 - 97: OoOoOO00 / IiiIIiiI11
   try :
    oo00oOO000oO0 [ III1ii1iII ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = III1ii1iII ( 'ignorecache' ) [ 0 ] . string
   except :
    I1 ( "Regex: -- no ignorecache" )
    if 71 - 71: II111iiii / i1IIi . ooO00oOoo % OoooooooOO . ii1IiI1i
  oo00oOO000oO0 = urllib . quote ( repr ( oo00oOO000oO0 ) )
  return oo00oOO000oO0
 except :
  oo00oOO000oO0 = None
  I1 ( 'regex Error: ' + OOO00O . encode ( 'utf-8' , 'ignore' ) )
def Iiiiii111i1ii ( url ) :
 try :
  for III1ii1iII in range ( 1 , 51 ) :
   iIIIiiI1i1i = i1i1iII1 ( url )
   if "EXT-X-STREAM-INF" in iIIIiiI1i1i : return url
   if not "EXTM3U" in iIIIiiI1i1i : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 25 - 25: iIii1I11I1II1 % IiiIIiiI11 . i1iIIi1
  if 14 - 14: O0OOo + ooO00oOoo - IiiIIiiI11 / O0 . IiiIII111ii
def i1iiIiI1Ii1i ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
 i1iIi = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 iiiii1II = True
 if 81 - 81: oO * IIIiiIIii + IiiIII111ii + OOooo000oo0 - OoooooooOO
 for i1i1I111iIi1 in i1iIi :
  if i1i1I111iIi1 in regexs :
   oo00O00oO000o = regexs [ i1i1I111iIi1 ]
   OOo00OoO = False
   if 10 - 10: IIIiiIIii / i11iIiiIii
   if 92 - 92: i1iIIII . IiiIII111ii
   if 'cookiejar' in oo00O00oO000o :
    OOo00OoO = oo00O00oO000o [ 'cookiejar' ]
    if '$doregex' in OOo00OoO :
     cookieJar = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     OOo00OoO = True
    else :
     OOo00OoO = True
   if OOo00OoO :
    if cookieJar == None :
     cookie_jar_file = None
     if 'open[' in oo00O00oO000o [ 'cookiejar' ] :
      cookie_jar_file = oo00O00oO000o [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 85 - 85: ooO00oOoo . IiiIII111ii
     cookieJar = O0O0Ooooo000 ( cookie_jar_file )
     if cookie_jar_file :
      o000oOoo0o000 ( cookieJar , cookie_jar_file )
    elif 'save[' in oo00O00oO000o [ 'cookiejar' ] :
     cookie_jar_file = oo00O00oO000o [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     IiI11iI1i1i1i = os . path . join ( IiII , cookie_jar_file )
     print 'complete_path' , IiI11iI1i1i1i
     o000oOoo0o000 ( cookieJar , cookie_jar_file )
     if 89 - 89: i1iIIII
     if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / OOooo000oo0 . i1iIIi1 % oooOOOOO
   if oo00O00oO000o [ 'page' ] and '$doregex' in oo00O00oO000o [ 'page' ] :
    oo00O00oO000o [ 'page' ] = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 50 - 50: iIii1I11I1II1 - oooOOOOO + i1iII1I1i1i1
   if 'setcookie' in oo00O00oO000o and oo00O00oO000o [ 'setcookie' ] and '$doregex' in oo00O00oO000o [ 'setcookie' ] :
    oo00O00oO000o [ 'setcookie' ] = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in oo00O00oO000o and oo00O00oO000o [ 'appendcookie' ] and '$doregex' in oo00O00oO000o [ 'appendcookie' ] :
    oo00O00oO000o [ 'appendcookie' ] = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 69 - 69: O0
    if 85 - 85: i1iIIi1 / O0
   if 'post' in oo00O00oO000o and '$doregex' in oo00O00oO000o [ 'post' ] :
    oo00O00oO000o [ 'post' ] = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    print 'post is now' , oo00O00oO000o [ 'post' ]
    if 18 - 18: IIIiiIIii % O0 * ooO00oOoo
   if 'rawpost' in oo00O00oO000o and '$doregex' in oo00O00oO000o [ 'rawpost' ] :
    oo00O00oO000o [ 'rawpost' ] = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 62 - 62: IiiIII111ii . oooOOOOO . OoooooooOO
   if 'rawpost' in oo00O00oO000o and '$epoctime$' in oo00O00oO000o [ 'rawpost' ] :
    oo00O00oO000o [ 'rawpost' ] = oo00O00oO000o [ 'rawpost' ] . replace ( '$epoctime$' , i111 ( ) )
    if 27 - 27: i11iIiiIii / ooO00oOoo
   if 'rawpost' in oo00O00oO000o and '$epoctime2$' in oo00O00oO000o [ 'rawpost' ] :
    oo00O00oO000o [ 'rawpost' ] = oo00O00oO000o [ 'rawpost' ] . replace ( '$epoctime2$' , oOoOOo ( ) )
    if 3 - 3: O0 / IiiIIiiI11
    if 31 - 31: i1iII1I1i1i1 + IIIiiIIii . OoooooooOO
   ooOooo0 = ''
   if oo00O00oO000o [ 'page' ] and oo00O00oO000o [ 'page' ] in cachedPages and not 'ignorecache' in oo00O00oO000o and forCookieJarOnly == False :
    ooOooo0 = cachedPages [ oo00O00oO000o [ 'page' ] ]
   else :
    if oo00O00oO000o [ 'page' ] and not oo00O00oO000o [ 'page' ] == '' and oo00O00oO000o [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in oo00O00oO000o [ 'page' ] :
      oo00O00oO000o [ 'page' ] = oo00O00oO000o [ 'page' ] . replace ( '$epoctime$' , i111 ( ) )
     if '$epoctime2$' in oo00O00oO000o [ 'page' ] :
      oo00O00oO000o [ 'page' ] = oo00O00oO000o [ 'page' ] . replace ( '$epoctime2$' , oOoOOo ( ) )
     oO0OO0 = oo00O00oO000o [ 'page' ] . split ( '|' )
     o0O0Oo00 = oO0OO0 [ 0 ]
     O0Oo0o000oO = None
     if len ( oO0OO0 ) > 1 :
      O0Oo0o000oO = oO0OO0 [ 1 ]
     iI111I11I1I1 = urllib2 . Request ( o0O0Oo00 )
     iI111I11I1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     if 'refer' in oo00O00oO000o :
      iI111I11I1I1 . add_header ( 'Referer' , oo00O00oO000o [ 'refer' ] )
     if 'agent' in oo00O00oO000o :
      iI111I11I1I1 . add_header ( 'User-agent' , oo00O00oO000o [ 'agent' ] )
     if 'x-req' in oo00O00oO000o :
      iI111I11I1I1 . add_header ( 'X-Requested-With' , oo00O00oO000o [ 'x-req' ] )
     if 'x-forward' in oo00O00oO000o :
      iI111I11I1I1 . add_header ( 'X-Forwarded-For' , oo00O00oO000o [ 'x-forward' ] )
     if 'setcookie' in oo00O00oO000o :
      print 'adding cookie' , oo00O00oO000o [ 'setcookie' ]
      iI111I11I1I1 . add_header ( 'Cookie' , oo00O00oO000o [ 'setcookie' ] )
     if 'appendcookie' in oo00O00oO000o :
      print 'appending cookie to cookiejar' , oo00O00oO000o [ 'appendcookie' ]
      oO0o00oOOooO0 = oo00O00oO000o [ 'appendcookie' ]
      oO0o00oOOooO0 = oO0o00oOOooO0 . split ( ';' )
      for OOOoO000 in oO0o00oOOooO0 :
       oOOOO , IiIi1ii111i1 = OOOoO000 . split ( '=' )
       i1i1i1I , oOOOO = oOOOO . split ( ':' )
       oOoo000 = cookielib . Cookie ( version = 0 , name = oOOOO , value = IiIi1ii111i1 , port = None , port_specified = False , domain = i1i1i1I , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( oOoo000 )
       if 87 - 87: OoooooooOO - IIIiiIIii / oooOOOOO . i11iIiiIii * OoooooooOO
     if 'origin' in oo00O00oO000o :
      iI111I11I1I1 . add_header ( 'Origin' , oo00O00oO000o [ 'origin' ] )
     if O0Oo0o000oO :
      O0Oo0o000oO = O0Oo0o000oO . split ( '&' )
      for OOOoO000 in O0Oo0o000oO :
       oOOOO , IiIi1ii111i1 = OOOoO000 . split ( '=' )
       iI111I11I1I1 . add_header ( oOOOO , IiIi1ii111i1 )
       if 84 - 84: ii1IiI1i / i1iIIII * IiiIIiiI11 / O0OOo - i11iIiiIii . OOooo000oo0
       if 60 - 60: ooO00oOoo * OoOoOO00
     if not cookieJar == None :
      I1iIiI11I1 = urllib2 . HTTPCookieProcessor ( cookieJar )
      i1oOOoo0o0OOOO = urllib2 . build_opener ( I1iIiI11I1 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      i1oOOoo0o0OOOO = urllib2 . install_opener ( i1oOOoo0o0OOOO )
      if 'noredirect' in oo00O00oO000o :
       i1IiII1III = urllib2 . build_opener ( I11i )
       i1oOOoo0o0OOOO = urllib2 . install_opener ( i1IiII1III )
       if 30 - 30: O0
     if 'connection' in oo00O00oO000o :
      print '..........................connection//////.' , oo00O00oO000o [ 'connection' ]
      from keepalive import HTTPHandler
      Oo00oo0000OO = HTTPHandler ( )
      i1oOOoo0o0OOOO = urllib2 . build_opener ( Oo00oo0000OO )
      urllib2 . install_opener ( i1oOOoo0o0OOOO )
     O0oOOo0Oo = None
     if 73 - 73: oO - IiiIII111ii
     if 'post' in oo00O00oO000o :
      O00oooo00o0O = oo00O00oO000o [ 'post' ]
      if '$LiveStreamRecaptcha' in O00oooo00o0O :
       ( ii1iii1I1I , oO0Ooo0ooOO0 ) = i1IIiIii1i ( oo00O00oO000o [ 'page' ] )
       if ii1iii1I1I :
        O00oooo00o0O += 'recaptcha_challenge_field:' + ii1iii1I1I + ',recaptcha_response_field:' + oO0Ooo0ooOO0
      ooOOO0OooOo = O00oooo00o0O . split ( ',' ) ;
      O0oOOo0Oo = { }
      for I1Ii in ooOOO0OooOo :
       oOOOO = I1Ii . split ( ':' ) [ 0 ] ;
       IiIi1ii111i1 = I1Ii . split ( ':' ) [ 1 ] ;
       O0oOOo0Oo [ oOOOO ] = IiIi1ii111i1
      O0oOOo0Oo = urllib . urlencode ( O0oOOo0Oo )
      if 70 - 70: OOooo000oo0 . OoooooooOO - IiiIIiiI11
     if 'rawpost' in oo00O00oO000o :
      O0oOOo0Oo = oo00O00oO000o [ 'rawpost' ]
      if '$LiveStreamRecaptcha' in O0oOOo0Oo :
       ( ii1iii1I1I , oO0Ooo0ooOO0 ) = i1IIiIii1i ( oo00O00oO000o [ 'page' ] )
       if ii1iii1I1I :
        O0oOOo0Oo += '&recaptcha_challenge_field=' + ii1iii1I1I + '&recaptcha_response_field=' + oO0Ooo0ooOO0
        if 30 - 30: ooO00oOoo % OoOoOO00
        if 89 - 89: IiiIII111ii + OoooooooOO + IiiIII111ii * i1IIi + iIii1I11I1II1 % i1iIIII
     if O0oOOo0Oo :
      OOooO0OOoo = urllib2 . urlopen ( iI111I11I1I1 , O0oOOo0Oo )
     else :
      OOooO0OOoo = urllib2 . urlopen ( iI111I11I1I1 )
      if 59 - 59: i1iII1I1i1i1 + i11iIiiIii
     ooOooo0 = OOooO0OOoo . read ( )
     ooOooo0 = oo0OOo0O ( ooOooo0 )
     if 'includeheaders' in oo00O00oO000o :
      ooOooo0 += str ( OOooO0OOoo . headers . get ( 'Set-Cookie' ) )
      if 39 - 39: OoooooooOO + O0OOo % i1iII1I1i1i1 / i1iII1I1i1i1
     OOooO0OOoo . close ( )
     cachedPages [ oo00O00oO000o [ 'page' ] ] = ooOooo0
     if 27 - 27: IiiIIiiI11 . i1iIIII . iIii1I11I1II1 . iIii1I11I1II1
     if forCookieJarOnly :
      return cookieJar
    elif oo00O00oO000o [ 'page' ] and not oo00O00oO000o [ 'page' ] . startswith ( 'http' ) :
     if oo00O00oO000o [ 'page' ] . startswith ( '$pyFunction:' ) :
      iIi1i = iI11i1I1 ( oo00O00oO000o [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar )
      if forCookieJarOnly :
       return cookieJar
      ooOooo0 = iIi1i
     else :
      ooOooo0 = oo00O00oO000o [ 'page' ]
   if '$pyFunction:playmedia(' in oo00O00oO000o [ 'expre' ] or 'ActivateWindow' in oo00O00oO000o [ 'expre' ] or any ( x in url for x in iIiiiI1IiI1I1 ) :
    iiiii1II = False
   if '$doregex' in oo00O00oO000o [ 'expre' ] :
    oo00O00oO000o [ 'expre' ] = i1iiIiI1Ii1i ( regexs , oo00O00oO000o [ 'expre' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 4 - 4: IiiIII111ii / i11iIiiIii / i1iII1I1i1i1
    if 91 - 91: iIii1I11I1II1 % IIIiiIIii . iIii1I11I1II1 % i1IIi / II111iiii * ii1IiI1i
   if not oo00O00oO000o [ 'expre' ] == '' :
    print 'doing it ' , oo00O00oO000o [ 'expre' ]
    if '$LiveStreamCaptcha' in oo00O00oO000o [ 'expre' ] :
     iIi1i = ii ( oo00O00oO000o , ooOooo0 , cookieJar )
     url = url . replace ( "$doregex[" + i1i1I111iIi1 + "]" , iIi1i )
    elif oo00O00oO000o [ 'expre' ] . startswith ( '$pyFunction:' ) :
     iIi1i = iI11i1I1 ( oo00O00oO000o [ 'expre' ] . split ( '$pyFunction:' ) [ 1 ] , ooOooo0 , cookieJar )
     if 'ActivateWindow' in oo00O00oO000o [ 'expre' ] : return
     print 'still hre'
     print 'url k val' , url , i1i1I111iIi1 , iIi1i
     if 81 - 81: O0 % oO
     url = url . replace ( "$doregex[" + i1i1I111iIi1 + "]" , iIi1i )
    else :
     if not ooOooo0 == '' :
      IiIII1i1i = re . compile ( oo00O00oO000o [ 'expre' ] ) . search ( ooOooo0 )
      iIi1i = ''
      try :
       iIi1i = IiIII1i1i . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     else :
      iIi1i = oo00O00oO000o [ 'expre' ]
     if rawPost :
      print 'rawpost'
      iIi1i = urllib . quote_plus ( iIi1i )
     if 'htmlunescape' in oo00O00oO000o :
      import HTMLParser
      iIi1i = HTMLParser . HTMLParser ( ) . unescape ( iIi1i )
     url = url . replace ( "$doregex[" + i1i1I111iIi1 + "]" , iIi1i )
   else :
    url = url . replace ( "$doregex[" + i1i1I111iIi1 + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , i111 ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , oOoOOo ( ) )
  if 41 - 41: OOooo000oo0 / oO * oO - i1iII1I1i1i1 . IiiIII111ii . OoooooooOO
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , I1iIIi111i1 ( cookieJar ) )
  if 12 - 12: II111iiii . i1iIIII / i1iII1I1i1i1
 if recursiveCall : return url
 print 'final url' , url
 if url == "" :
  return
 else :
  return url , iiiii1II
  if 77 - 77: i1iIIi1 - OoOoOO00 % i1iIIII - O0
  if 67 - 67: i1iII1I1i1i1 + OOooo000oo0
  if 84 - 84: O0 * OoooooooOO - oooOOOOO * oooOOOOO
def i1ii ( t ) :
 import hashlib
 OOOoO000 = hashlib . md5 ( )
 OOOoO000 . update ( t )
 return OOOoO000 . hexdigest ( )
 if 65 - 65: ii1IiI1i / i1 % oooOOOOO
def iIiIIii ( encrypted ) :
 OOo00 = ""
 for iIi1i in encrypted . split ( ':' ) :
  OOo00 += chr ( int ( iIi1i . replace ( "0m0" , "" ) ) / 84 / 5 )
 return OOo00
 if 37 - 37: i1IIi
def III1i1iI1 ( media_url ) :
 try :
  import CustomPlayer
  o0ooo00o = CustomPlayer . MyXBMCPlayer ( )
  oOO00oO00O0OO = xbmcgui . ListItem ( label = str ( OOO00O ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  o0ooo00o . play ( media_url , oOO00oO00O0OO )
  xbmc . sleep ( 1000 )
  while o0ooo00o . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 96 - 96: ii1IiI1i
o0OO0oO0oOO0O = I11iIi1I . getSetting ( 'inicio' )
i1I11 = base64 . b32decode ( o0OO0oO0oOO0O )
if 39 - 39: oO * i1iIIi1 / ii1IiI1i * i1 . i1iIIII % II111iiii
def O0OoOoO00O ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  OooOOO0O00 = page_value
  page_value = i1i1iII1 ( page_value , headers = referer )
  if 29 - 29: IIIiiIIii % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / IiiIIiiI11
 oo0o0000Oo0 = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 80 - 80: IiiIII111ii - OOooo000oo0
 OOooO = re . compile ( oo0o0000Oo0 ) . findall ( page_value )
 ooOOoO = ""
 if OOooO and len ( OOooO ) > 0 :
  for IiIi1ii111i1 in OOooO :
   O00O0OO00oo = oOOO ( IiIi1ii111i1 )
   ooo0oooo0 = OOoO ( O00O0OO00oo , '\'(.*?)\'' )
   if 'unescape' in O00O0OO00oo :
    O00O0OO00oo = urllib . unquote ( ooo0oooo0 )
   ooOOoO += O00O0OO00oo + '\n'
  print 'final value is ' , ooOOoO
  if 62 - 62: ooO00oOoo + oO + i1IIi / OoooooooOO
  OooOOO0O00 = OOoO ( ooOOoO , 'src="(.*?)"' )
  if 7 - 7: IIIiiIIii + i1IIi . OoOoOO00 / OOooo000oo0
  page_value = i1i1iII1 ( OooOOO0O00 , headers = referer )
  if 22 - 22: i1iIIi1 - i1iIIi1 % i1iII1I1i1i1 . IiiIII111ii + O0OOo
 Oo00OOo00O = OOoO ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 o0 = OOoO ( page_value , 'file\',\s\'(.*?)\'' )
 if 20 - 20: OoooooooOO * IIIiiIIii * O0 . i1iII1I1i1i1
 if 78 - 78: iIii1I11I1II1 + i1iIIII - oO * IiiIII111ii - OoooooooOO % ii1IiI1i
 return Oo00OOo00O + ' playpath=' + o0 + ' pageUrl=' + OooOOO0O00
 if 34 - 34: O0
def OooOOOo0 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = i1i1iII1 ( page_value , headers = referer )
 oo0o0000Oo0 = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 OOooO = re . compile ( oo0o0000Oo0 ) . findall ( page_value ) [ 0 ]
 if 54 - 54: oO - i1iIIII - IiiIII111ii . iIii1I11I1II1
 oOOOoo00 , oo000OO00Oo , ooo , o0OIIiI1I1 , I11I1IIiiII1 , IiIi1ii111i1 = ( OOooO )
 I11I1IIiiII1 = int ( I11I1IIiiII1 )
 oOOOoo00 = int ( oOOOoo00 ) / I11I1IIiiII1
 oo000OO00Oo = int ( oo000OO00Oo ) / I11I1IIiiII1
 ooo = int ( ooo ) / I11I1IIiiII1
 o0OIIiI1I1 = int ( o0OIIiI1I1 ) / I11I1IIiiII1
 if 31 - 31: OoOoOO00 * O0OOo + OoooooooOO - IiiIIiiI11 / OoooooooOO
 I111IIiii1Ii = 'rtmp://' + str ( oOOOoo00 ) + '.' + str ( oo000OO00Oo ) + '.' + str ( ooo ) + '.' + str ( o0OIIiI1I1 ) + IiIi1ii111i1 ;
 return I111IIiii1Ii
 if 13 - 13: O0OOo . OoOoOO00 * O0OOo + OoOoOO00
def OoOooo ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 o00 = os . path . join ( IiII , 'testfile.m3u' )
 str += '\n'
 oo00OOoOoO00 ( o00 , str )
 return o00
 if 15 - 15: oooOOOOO / O0 . IIIiiIIii . i11iIiiIii
def oo00OOoOoO00 ( file_name , page_data , append = False ) :
 if append :
  I11I1IIiiII1 = open ( file_name , 'a' )
  I11I1IIiiII1 . write ( page_data )
  I11I1IIiiII1 . close ( )
 else :
  I11I1IIiiII1 = open ( file_name , 'wb' )
  I11I1IIiiII1 . write ( page_data )
  I11I1IIiiII1 . close ( )
  return ''
  if 59 - 59: IiiIII111ii - IIIiiIIii - i1iIIi1
def Ii11iI ( file_name ) :
 I11I1IIiiII1 = open ( file_name , 'rb' )
 o0OIIiI1I1 = I11I1IIiiII1 . read ( )
 I11I1IIiiII1 . close ( )
 return o0OIIiI1I1
 if 52 - 52: i1iII1I1i1i1 - IiiIIiiI11 * O0OOo
def Ii1I11I ( page_data ) :
 import re , base64 , urllib ;
 iiIii1I = page_data
 while 'geh(' in iiIii1I :
  if iiIii1I . startswith ( 'lol(' ) : iiIii1I = iiIii1I [ 5 : - 1 ]
  if 47 - 47: i1iIIi1 . i1iIIII / IIIiiIIii
  iiIii1I = re . compile ( '"(.*?)"' ) . findall ( iiIii1I ) [ 0 ] ;
  iiIii1I = base64 . b64decode ( iiIii1I ) ;
  iiIii1I = urllib . unquote ( iiIii1I ) ;
 print iiIii1I
 return iiIii1I
 if 83 - 83: IIIiiIIii / i1iII1I1i1i1 / i1iII1I1i1i1 + IIIiiIIii * IiiIII111ii + IIIiiIIii
def IIIIiii ( page_data ) :
 print 'get_dag_url2' , page_data
 oO0o = i1i1iII1 ( page_data ) ;
 IIIii1iiIi = '(http.*)'
 import uuid
 oooo0OOo = str ( uuid . uuid1 ( ) ) . upper ( )
 OoO00 = re . compile ( IIIii1iiIi ) . findall ( oO0o )
 I11iIi1II = [ ( 'X-Playback-Session-Id' , oooo0OOo ) ]
 for ooo0OOiIi1IiI in OoO00 :
  try :
   I11IIIiIi11 = i1i1iII1 ( ooo0OOiIi1IiI , headers = I11iIi1II ) ;
   if 39 - 39: oO % O0 % ii1IiI1i . i1IIi
  except : pass
  if 86 - 86: i1 * OoooooooOO
 return page_data + '|&X-Playback-Session-Id=' + oooo0OOo
 if 71 - 71: iIii1I11I1II1 - i1iII1I1i1i1 . OoOoOO00 % OoooooooOO + i1iII1I1i1i1
 if 26 - 26: OOooo000oo0 + i1iII1I1i1i1 / i1 % ii1IiI1i % ooO00oOoo + II111iiii
def i11I1I1iiI ( page_data ) :
 print 'get_dag_url' , page_data
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  I11iIi1II = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = i1i1iII1 ( page_data , headers = I11iIi1II ) ;
  if 34 - 34: i1iIIII % i1iIIi1 . O0 . iIii1I11I1II1
 if '127.0.0.1' in page_data :
  return oo ( page_data )
 elif OOoO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  i1II1I = OOoO ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + OOoO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + OOoO ( page_data , '\\?y=([^&]+)&' )
 else :
  i1II1I = OOoO ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( i1II1I ) == 0 :
   i1II1I = page_data
 i1II1I = i1II1I . replace ( ' ' , '%20' )
 return i1II1I
 if 95 - 95: i1 - i1iII1I1i1i1 / II111iiii % ooO00oOoo . IIIiiIIii
def OOoO ( data , re_patten ) :
 oOOo0O00o = ''
 oo00O00oO000o = re . search ( re_patten , data )
 if oo00O00oO000o != None :
  oOOo0O00o = oo00O00oO000o . group ( 1 )
 else :
  oOOo0O00o = ''
 return oOOo0O00o
 if 24 - 24: i1IIi . i11iIiiIii
def oo ( page_data ) :
 i1II1I = ''
 if '127.0.0.1' in page_data :
  i1II1I = OOoO ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + OOoO ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 16 - 16: OOooo000oo0 % ooO00oOoo + i1iIIII - O0 . IiiIIiiI11 / IiiIII111ii
 if OOoO ( page_data , 'token=([^&]+)&' ) != '' :
  i1II1I = i1II1I + '?token=' + OOoO ( page_data , 'token=([^&]+)&' )
 elif OOoO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  i1II1I = OOoO ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + OOoO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + OOoO ( page_data , '\\?y=([^&]+)&' )
 else :
  i1II1I = OOoO ( page_data , 'HREF="([^"]+)"' )
  if 35 - 35: O0OOo / IiiIII111ii / II111iiii - iIii1I11I1II1 + II111iiii . IiiIII111ii
 if 'dag1.asx' in i1II1I :
  return i11I1I1iiI ( i1II1I )
  if 81 - 81: IiiIIiiI11 * i1iII1I1i1i1 - ooO00oOoo * oO % ii1IiI1i * ii1IiI1i
 if 'devinlivefs.fplive.net' not in i1II1I :
  i1II1I = i1II1I . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in i1II1I :
  i1II1I = i1II1I . replace ( 'permlive' , 'flive' )
 return i1II1I
 if 59 - 59: iIii1I11I1II1
 if 7 - 7: i1iII1I1i1i1 * OoOoOO00 / IIIiiIIii * i11iIiiIii
def o00II1i111 ( str_eval ) :
 i1iiiIii11 = ""
 try :
  OOoOOO000O0 = "w,i,s,e=(" + str_eval + ')'
  exec ( OOoOOO000O0 )
  i1iiiIii11 = oOo0 ( w , i , s , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 48 - 48: OOooo000oo0 - OoooooooOO % i1iII1I1i1i1 * ii1IiI1i
 return i1iiiIii11
 if 69 - 69: i1IIi
def oOo0 ( w , i , s , e ) :
 ooOoOOOOo = 0 ;
 ooooOooooOOo = 0 ;
 ooO00O00oOO = 0 ;
 I1IIII1ii = [ ] ;
 IiIIi1I1I11Ii = [ ] ;
 while True :
  if ( ooOoOOOOo < 5 ) :
   IiIIi1I1I11Ii . append ( w [ ooOoOOOOo ] )
  elif ( ooOoOOOOo < len ( w ) ) :
   I1IIII1ii . append ( w [ ooOoOOOOo ] ) ;
  ooOoOOOOo += 1 ;
  if ( ooooOooooOOo < 5 ) :
   IiIIi1I1I11Ii . append ( i [ ooooOooooOOo ] )
  elif ( ooooOooooOOo < len ( i ) ) :
   I1IIII1ii . append ( i [ ooooOooooOOo ] )
  ooooOooooOOo += 1 ;
  if ( ooO00O00oOO < 5 ) :
   IiIIi1I1I11Ii . append ( s [ ooO00O00oOO ] )
  elif ( ooO00O00oOO < len ( s ) ) :
   I1IIII1ii . append ( s [ ooO00O00oOO ] ) ;
  ooO00O00oOO += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( I1IIII1ii ) + len ( IiIIi1I1I11Ii ) + len ( e ) ) :
   break ;
   if 64 - 64: OoooooooOO
 oO0oooooo = '' . join ( I1IIII1ii )
 o0OO0Oo = '' . join ( IiIIi1I1I11Ii )
 ooooOooooOOo = 0 ;
 I11iiii1I = [ ] ;
 for ooOoOOOOo in range ( 0 , len ( I1IIII1ii ) , 2 ) :
  iiiiI1iiiIi = - 1 ;
  if ( ord ( o0OO0Oo [ ooooOooooOOo ] ) % 2 ) :
   iiiiI1iiiIi = 1 ;
  I11iiii1I . append ( chr ( int ( oO0oooooo [ ooOoOOOOo : ooOoOOOOo + 2 ] , 36 ) - iiiiI1iiiIi ) ) ;
  ooooOooooOOo += 1 ;
  if ( ooooOooooOOo >= len ( IiIIi1I1I11Ii ) ) :
   ooooOooooOOo = 0 ;
 I111IIiii1Ii = '' . join ( I11iiii1I )
 if 'eval(function(w,i,s,e)' in I111IIiii1Ii :
  print 'STILL GOing'
  I111IIiii1Ii = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( I111IIiii1Ii ) [ 0 ]
  return o00II1i111 ( I111IIiii1Ii )
 else :
  print 'FINISHED'
  return I111IIiii1Ii
  if 84 - 84: i1iII1I1i1i1
def oOOO ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  o0OoO00 = None
  if page_value . startswith ( "http" ) :
   page_value = i1i1iII1 ( page_value )
  print 'page_value' , page_value
  if regex_for_text and len ( regex_for_text ) > 0 :
   page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   if 18 - 18: O0OOo - IIIiiIIii - OoOoOO00 - OoOoOO00
  page_value = OOooo00 ( page_value , iterations , total_iteration )
 except : traceback . print_exc ( file = sys . stdout )
 print 'unpacked' , page_value
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  print 'sav1 unpacked' , page_value
 return page_value
 if 35 - 35: IiiIII111ii . ii1IiI1i * i11iIiiIii
def OOooo00 ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 print 'iteration' , iteration
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  iiII = sJavascript . split ( 'var _0xcb8a=' )
  OOoOOO000O0 = "myarray=" + iiII [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( OOoOOO000O0 )
  o0Oii1111i = 62
  O0ooOO = int ( iiII [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  IiiI = myarray [ 0 ]
  i11ii = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as i11I1 :
   i11I1 . write ( str ( i11ii ) )
 else :
  if 34 - 34: O0 * O0 % OoooooooOO + IiiIIiiI11 * iIii1I11I1II1 % oO
  iiII = sJavascript . split ( "rn p}('" )
  print iiII
  if 25 - 25: i1iIIII + ii1IiI1i . IIIiiIIii % ii1IiI1i * i1iII1I1i1i1
  IiiI , o0Oii1111i , O0ooOO , i11ii = ( '' , '0' , '0' , '' )
  if 32 - 32: i11iIiiIii - IiiIII111ii
  OOoOOO000O0 = "p1,a1,c1,k1=('" + iiII [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( OOoOOO000O0 )
 i11ii = i11ii . split ( '|' )
 iiII = iiII [ 1 ] . split ( "))'" )
 oOOoO0 = ''
 o0OIIiI1I1 = ''
 oo00ooOoo = str ( iii1IIIiiiI ( IiiI , o0Oii1111i , O0ooOO , i11ii , oOOoO0 , o0OIIiI1I1 , iteration ) )
 if iteration >= totaliterations :
  return oo00ooOoo
 else :
  return OOooo00 ( oo00ooOoo , iteration + 1 )
  if 94 - 94: O0 - i1iIIII - iIii1I11I1II1 % i1iIIi1 / oO % IiiIIiiI11
def iii1IIIiiiI ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 44 - 44: OOooo000oo0 % iIii1I11I1II1
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   oo0ooO0 = str ( IIiiiiIiIIii ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + oo0ooO0 + '\\b' , k [ c ] , p )
   else :
    p = O0OO ( p , oo0ooO0 , k [ c ] )
    if 39 - 39: ooO00oOoo + OoOoOO00 - iIii1I11I1II1 - IIIiiIIii
 return p
 if 7 - 7: oooOOOOO . ii1IiI1i / ooO00oOoo . i1iII1I1i1i1 * i1iIIII - II111iiii
def O0OO ( source_str , word_to_find , replace_with ) :
 I1ii1iI1II11ii = None
 I1ii1iI1II11ii = source_str . split ( word_to_find )
 if len ( I1ii1iI1II11ii ) > 1 :
  i1i1IiIiIi1Ii = [ ]
  oO0ooOO = 0
  for IIi1iI1 in I1ii1iI1II11ii :
   if 44 - 44: ooO00oOoo - oO / II111iiii * i1 * OOooo000oo0
   i1i1IiIiIi1Ii . append ( IIi1iI1 )
   iIi1i = word_to_find
   if 73 - 73: IIIiiIIii - OoOoOO00 * i1IIi / i11iIiiIii * i1iII1I1i1i1 % II111iiii
   if oO0ooOO == len ( I1ii1iI1II11ii ) - 1 :
    iIi1i = ''
   else :
    if len ( IIi1iI1 ) == 0 :
     if ( len ( I1ii1iI1II11ii [ oO0ooOO + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( I1ii1iI1II11ii [ oO0ooOO + 1 ] ) > 0 and I1ii1iI1II11ii [ oO0ooOO + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      iIi1i = replace_with
    else :
     if ( I1ii1iI1II11ii [ oO0ooOO ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( I1ii1iI1II11ii [ oO0ooOO + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( I1ii1iI1II11ii [ oO0ooOO + 1 ] ) > 0 and I1ii1iI1II11ii [ oO0ooOO + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      iIi1i = replace_with
      if 56 - 56: OoooooooOO * OOooo000oo0 . OOooo000oo0 . ooO00oOoo
   i1i1IiIiIi1Ii . append ( iIi1i )
   oO0ooOO += 1
  source_str = '' . join ( i1i1IiIiIi1Ii )
 return source_str
 if 24 - 24: OOooo000oo0 . i1iIIII * oO % IiiIIiiI11 / i1iII1I1i1i1
def Oo0Ooo0O0 ( num , radix ) :
 iIIIiiI1i1i = ""
 if num == 0 : return '0'
 while num > 0 :
  iIIIiiI1i1i = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + iIIIiiI1i1i
  num /= radix
 return iIIIiiI1i1i
 if 42 - 42: i1IIi * O0OOo - oO . OoOoOO00 + IIIiiIIii . iIii1I11I1II1
def IIiiiiIiIIii ( cc , a ) :
 oo0ooO0 = "" if cc < a else IIiiiiIiIIii ( int ( cc / a ) , a )
 cc = ( cc % a )
 o0iIiiIiiIi = chr ( cc + 29 ) if cc > 35 else str ( Oo0Ooo0O0 ( cc , 36 ) )
 return oo0ooO0 + o0iIiiIiiIi
 if 40 - 40: IIIiiIIii
 if 78 - 78: iIii1I11I1II1
def I1iIIi111i1 ( cookieJar ) :
 try :
  ooO0oo0o0 = ""
  for i111IiI1I , IIiIii1 in enumerate ( cookieJar ) :
   ooO0oo0o0 += IIiIii1 . name + "=" + IIiIii1 . value + ";"
 except : pass
 return ooO0oo0o0
 if 62 - 62: iIii1I11I1II1 + IiiIIiiI11 . OOooo000oo0 / oooOOOOO % O0 . IiiIII111ii
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + IIIiiIIii / IIIiiIIii / II111iiii
def o000oOoo0o000 ( cookieJar , COOKIEFILE ) :
 try :
  IiI11iI1i1i1i = os . path . join ( IiII , COOKIEFILE )
  cookieJar . save ( IiI11iI1i1i1i , ignore_discard = True )
 except : pass
 if 49 - 49: i1iII1I1i1i1 . ooO00oOoo . i11iIiiIii - II111iiii / oO
def O0O0Ooooo000 ( COOKIEFILE ) :
 if 62 - 62: i1iII1I1i1i1
 i1I1i = None
 if COOKIEFILE :
  try :
   IiI11iI1i1i1i = os . path . join ( IiII , COOKIEFILE )
   i1I1i = cookielib . LWPCookieJar ( )
   i1I1i . load ( IiI11iI1i1i1i , ignore_discard = True )
  except :
   i1I1i = None
   if 87 - 87: OOooo000oo0 / O0 * oooOOOOO / IIIiiIIii
 if not i1I1i :
  i1I1i = cookielib . LWPCookieJar ( )
  if 19 - 19: IiiIII111ii + i1IIi . OoOoOO00 - OOooo000oo0
 return i1I1i
 if 16 - 16: O0OOo + i1iIIi1 / IIIiiIIii
def iI11i1I1 ( fun_call , page_data , Cookie_Jar ) :
 O00oOoo0OoO0 = ''
 if Oo0oO0ooo not in sys . path :
  sys . path . append ( Oo0oO0ooo )
  if 62 - 62: i1IIi / i1iIIi1 . OoOoOO00 * IIIiiIIii
 print fun_call
 try :
  i11i1Ii1 = 'import ' + fun_call . split ( '.' ) [ 0 ]
  print i11i1Ii1 , sys . path
  exec ( i11i1Ii1 )
  print 'done'
 except :
  print 'error in import'
  traceback . print_exc ( file = sys . stdout )
 print 'ret_val=' + fun_call
 exec ( 'ret_val=' + fun_call )
 print O00oOoo0OoO0
 if 98 - 98: IiiIII111ii
 return str ( O00oOoo0OoO0 )
 if 92 - 92: IiiIII111ii - iIii1I11I1II1
def i1IIiIii1i ( url ) :
 I11III111i = i1i1iII1 ( url )
 o0Oo = ""
 o0O0 = ""
 I1I1Iiii1 = "<script.*?src=\"(.*?recap.*?)\""
 oOOo0O00o = re . findall ( I1I1Iiii1 , I11III111i )
 i111i1 = False
 OoOoOo0 = None
 o0O0 = None
 if 39 - 39: i1iIIII - ooO00oOoo
 if oOOo0O00o and len ( oOOo0O00o ) > 0 :
  OOO0o0OO0OO = oOOo0O00o [ 0 ]
  i111i1 = True
  if 64 - 64: II111iiii
  iIIIiIi1I1i = 'challenge.*?\'(.*?)\''
  OoOOoO0oOo = '\'(.*?)\''
  O0ooOOOO0O0 = i1i1iII1 ( OOO0o0OO0OO )
  o0Oo = re . findall ( iIIIiIi1I1i , O0ooOOOO0O0 ) [ 0 ]
  i1IIi1i1Ii1 = 'http://www.google.com/recaptcha/api/reload?c=' ;
  Iii = OOO0o0OO0OO . split ( 'k=' ) [ 1 ]
  i1IIi1i1Ii1 += o0Oo + '&k=' + Iii + '&captcha_k=1&type=image&lang=en-GB'
  o0Oo0oO = i1i1iII1 ( i1IIi1i1Ii1 )
  OoOoOo0 = re . findall ( OoOOoO0oOo , o0Oo0oO ) [ 0 ]
  iIII1iiIi11 = 'http://www.google.com/recaptcha/api/image?c=' + OoOoOo0
  if not iIII1iiIi11 . startswith ( "http" ) :
   iIII1iiIi11 = 'http://www.google.com/recaptcha/api/' + iIII1iiIi11
  import random
  oOOOO = random . randrange ( 100 , 1000 , 5 )
  ooOo0O0O0oOO0 = os . path . join ( IiII , str ( oOOOO ) + "captcha.img" )
  iIiIIi = open ( ooOo0O0O0oOO0 , "wb" )
  iIiIIi . write ( i1i1iII1 ( iIII1iiIi11 ) )
  iIiIIi . close ( )
  III1I = I1I111iIi ( captcha = ooOo0O0O0oOO0 )
  o0O0 = III1I . get ( )
  os . remove ( ooOo0O0O0oOO0 )
 return OoOoOo0 , o0O0
 if 53 - 53: iIii1I11I1II1 + IIIiiIIii - ii1IiI1i - O0OOo / i1iIIi1 % i11iIiiIii
def i1i1iII1 ( url , cookieJar = None , post = None , timeout = 20 , headers = None ) :
 if 3 - 3: IiiIIiiI11 . i1iIIi1 % OoOoOO00 + ooO00oOoo
 if 64 - 64: i1IIi
 I1iIiI11I1 = urllib2 . HTTPCookieProcessor ( cookieJar )
 i1oOOoo0o0OOOO = urllib2 . build_opener ( I1iIiI11I1 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 iI111I11I1I1 = urllib2 . Request ( url )
 iI111I11I1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for OOOoO000 , IIii1 in headers :
   iI111I11I1I1 . add_header ( OOOoO000 , IIii1 )
   if 35 - 35: i11iIiiIii - OoOoOO00 / i1iII1I1i1i1 + oO * O0OOo
 OOooO0OOoo = i1oOOoo0o0OOOO . open ( iI111I11I1I1 , post , timeout = timeout )
 ooOooo0 = OOooO0OOoo . read ( )
 OOooO0OOoo . close ( )
 return ooOooo0 ;
 if 49 - 49: IIIiiIIii * oO + i1iIIII + IiiIIiiI11
def IIi11 ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 ooo0O0OOO000o = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 iiI1iii = '' ;
 for III1ii1iII in range ( len ( ooo0O0OOO000o ) ) :
  iiI1iii += chr ( ord ( ooo0O0OOO000o [ III1ii1iII ] ) - ooo0O0OOO000o [ len ( ooo0O0OOO000o ) - 1 ] ) ;
 iiI1iii = urllib . unquote ( iiI1iii )
 print iiI1iii
 return iiI1iii
 if 79 - 79: i1 * ii1IiI1i . OoooooooOO - i1iIIII * IIIiiIIii
def oo0OOo0O ( str ) :
 o000o0O0Oo00 = re . findall ( 'unescape\(\'(.*?)\'' , str )
 print 'js' , o000o0O0Oo00
 if ( not o000o0O0Oo00 == None ) and len ( o000o0O0Oo00 ) > 0 :
  for ooOOoOo in o000o0O0Oo00 :
   str = str . replace ( ooOOoOo , urllib . unquote ( ooOOoOo ) )
 return str
 if 90 - 90: II111iiii / OoOoOO00
iiiOOoo = 0
def ii ( m , html_page , cookieJar ) :
 global iiiOOoo
 iiiOOoo += 1
 ooOO = m [ 'expre' ]
 OooOOO0O00 = m [ 'page' ]
 i1iiIiI = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( ooOO ) [ 0 ]
 if 60 - 60: O0OOo % IiiIIiiI11 / i1iII1I1i1i1 % i1iIIi1 - ii1IiI1i % iIii1I11I1II1
 OOO0o0OO0OO = re . compile ( i1iiIiI ) . findall ( html_page ) [ 0 ]
 print ooOO , i1iiIiI , OOO0o0OO0OO
 if not OOO0o0OO0OO . startswith ( "http" ) :
  OO00Ooo = 'http://' + "" . join ( OooOOO0O00 . split ( '/' ) [ 2 : 3 ] )
  if OOO0o0OO0OO . startswith ( "/" ) :
   OOO0o0OO0OO = OO00Ooo + OOO0o0OO0OO
  else :
   OOO0o0OO0OO = OO00Ooo + '/' + OOO0o0OO0OO
   if 87 - 87: OOooo000oo0 * i1iII1I1i1i1 % oooOOOOO % ii1IiI1i
 ooOo0O0O0oOO0 = os . path . join ( IiII , str ( iiiOOoo ) + "captcha.jpg" )
 iIiIIi = open ( ooOo0O0O0oOO0 , "wb" )
 print ' c capurl' , OOO0o0OO0OO
 iI111I11I1I1 = urllib2 . Request ( OOO0o0OO0OO )
 iI111I11I1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'refer' in m :
  iI111I11I1I1 . add_header ( 'Referer' , m [ 'refer' ] )
 if 'agent' in m :
  iI111I11I1I1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  iI111I11I1I1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 4 - 4: ii1IiI1i + oO / O0OOo
 urllib2 . urlopen ( iI111I11I1I1 )
 OOooO0OOoo = urllib2 . urlopen ( iI111I11I1I1 )
 if 13 - 13: IiiIIiiI11
 iIiIIi . write ( OOooO0OOoo . read ( ) )
 OOooO0OOoo . close ( )
 iIiIIi . close ( )
 III1I = I1I111iIi ( captcha = ooOo0O0O0oOO0 )
 o0O0 = III1I . get ( )
 return o0O0
 if 80 - 80: oO - IIIiiIIii
class I1I111iIi ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 41 - 41: IIIiiIIii - OOooo000oo0 * OoOoOO00
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   OO0OoOo0OOO = self . kbd . getText ( )
   self . close ( )
   return OO0OoOo0OOO
  self . close ( )
  return False
  if 47 - 47: OoooooooOO % O0 * IiiIIiiI11 . oO
def i111 ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 38 - 38: O0 - oooOOOOO % IiiIII111ii
def oOoOOo ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 64 - 64: iIii1I11I1II1
def IIi1iI ( ) :
 oO0Ooo0OooOOo = [ ]
 O00o0O = sys . argv [ 2 ]
 if len ( O00o0O ) >= 2 :
  iIIIiI = sys . argv [ 2 ]
  O00 = iIIIiI . replace ( '?' , '' )
  if ( iIIIiI [ len ( iIIIiI ) - 1 ] == '/' ) :
   iIIIiI = iIIIiI [ 0 : len ( iIIIiI ) - 2 ]
  i1iiIII1IIiIIII = O00 . split ( '&' )
  oO0Ooo0OooOOo = { }
  for III1ii1iII in range ( len ( i1iiIII1IIiIIII ) ) :
   I1iIIII1 = { }
   I1iIIII1 = i1iiIII1IIiIIII [ III1ii1iII ] . split ( '=' )
   if ( len ( I1iIIII1 ) ) == 2 :
    oO0Ooo0OooOOo [ I1iIIII1 [ 0 ] ] = I1iIIII1 [ 1 ]
 return oO0Ooo0OooOOo
 if 57 - 57: ii1IiI1i . iIii1I11I1II1 % i1iIIi1 % oO * ii1IiI1i
 if 8 - 8: ii1IiI1i . i1iIIi1 % O0OOo . OoOoOO00 % OoOoOO00 . oO
def I1I11ii ( ) :
 iii = json . loads ( open ( i1i1II ) . read ( ) )
 oOooOOOoOo = len ( iii )
 for III1ii1iII in iii :
  OOO00O = III1ii1iII [ 0 ]
  ooOO00O00oo = III1ii1iII [ 1 ]
  OOoOoo00Oo = III1ii1iII [ 2 ]
  try :
   oOOo0 = III1ii1iII [ 3 ]
   if oOOo0 == None :
    raise
  except :
   if I11iIi1I . getSetting ( 'use_thumb' ) == "true" :
    oOOo0 = OOoOoo00Oo
   else :
    oOOo0 = i11Iiii
  try : iIO0O0Oooo0o = III1ii1iII [ 5 ]
  except : iIO0O0Oooo0o = None
  try : oo00oOO000oO0 = III1ii1iII [ 6 ]
  except : oo00oOO000oO0 = None
  if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
  if III1ii1iII [ 4 ] == 0 :
   oooooo0O000o ( ooOO00O00oo , OOO00O , OOoOoo00Oo , oOOo0 , '' , '' , '' , 'fav' , iIO0O0Oooo0o , oo00oOO000oO0 , oOooOOOoOo )
  else :
   Ii1I ( OOO00O , ooOO00O00oo , III1ii1iII [ 4 ] , OOoOoo00Oo , i11Iiii , '' , '' , '' , '' , 'fav' )
   if 18 - 18: i1 . II111iiii % ii1IiI1i % oO
   if 87 - 87: iIii1I11I1II1 . OoooooooOO * ii1IiI1i
def OOOo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 o0ooOo00O = [ ]
 if not os . path . exists ( i1i1II + 'txt' ) :
  os . makedirs ( i1i1II + 'txt' )
 if not os . path . exists ( O0oo0OO0 ) :
  os . makedirs ( O0oo0OO0 )
 try :
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1i1II ) == False :
  I1 ( 'Making Favorites File' )
  o0ooOo00O . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOOOoo00 = open ( i1i1II , "w" )
  oOOOoo00 . write ( json . dumps ( o0ooOo00O ) )
  oOOOoo00 . close ( )
 else :
  I1 ( 'Appending Favorites' )
  oOOOoo00 = open ( i1i1II ) . read ( )
  iIii1 = json . loads ( oOOOoo00 )
  iIii1 . append ( ( name , url , iconimage , fanart , mode ) )
  oo000OO00Oo = open ( i1i1II , "w" )
  oo000OO00Oo . write ( json . dumps ( iIii1 ) )
  oo000OO00Oo . close ( )
  if 38 - 38: iIii1I11I1II1 + i11iIiiIii * i1 * i1iIIi1 % i1iII1I1i1i1
  if 5 - 5: i1iIIi1 - IiiIII111ii + OoOoOO00 * O0 / OOooo000oo0 - oO
def OoO0oO00o ( name ) :
 iIii1 = json . loads ( open ( i1i1II ) . read ( ) )
 for i111IiI1I in range ( len ( iIii1 ) ) :
  if iIii1 [ i111IiI1I ] [ 0 ] == name :
   del iIii1 [ i111IiI1I ]
   oo000OO00Oo = open ( i1i1II , "w" )
   oo000OO00Oo . write ( json . dumps ( iIii1 ) )
   oo000OO00Oo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 10 - 10: i1
def Ii1iI111II1I1 ( url ) :
 if I11iIi1I . getSetting ( 'Updatecommonresolvers' ) == 'true' :
  ooo0OOiIi1IiI = os . path . join ( iI1Ii11111iIi , 'genesisresolvers.py' )
  if xbmcvfs . exists ( ooo0OOiIi1IiI ) :
   os . remove ( ooo0OOiIi1IiI )
   if 22 - 22: i11iIiiIii / O0
  O0O0o0oO0O00 = 'https://raw.githubusercontent.com/lambda81/lambda-addons/master/plugin.video.genesis/commonresolvers.py'
  o0O0oO0 = urllib . urlretrieve ( O0O0o0oO0O00 , ooo0OOiIi1IiI )
  I11iIi1I . setSetting ( 'Updatecommonresolvers' , 'false' )
 try :
  import genesisresolvers
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,Atualize o commonresolvers para continuar. - ,10000)" )
  if 77 - 77: O0 . oO
 i1i1IiIi1 = genesisresolvers . get ( url ) . result
 if url == i1i1IiIi1 or i1i1IiIi1 is None :
  xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,Usando Urlresolver.. - ,5000)" )
  import urlresolver
  I1iiIiI1iI1I = urlresolver . HostedMediaFile ( url )
  if I1iiIiI1iI1I :
   o00ooO = urlresolver . resolve ( url )
   i1i1IiIi1 = o00ooO
 if i1i1IiIi1 :
  if isinstance ( i1i1IiIi1 , list ) :
   for i1i1I111iIi1 in i1i1IiIi1 :
    III1II111Ii1 = I11iIi1I . getSetting ( 'quality' )
    if i1i1I111iIi1 [ 'quality' ] == 'HD' :
     o00ooO = i1i1I111iIi1 [ 'url' ]
     break
    elif i1i1I111iIi1 [ 'quality' ] == 'SD' :
     o00ooO = i1i1I111iIi1 [ 'url' ]
    elif i1i1I111iIi1 [ 'quality' ] == '1080p' and I11iIi1I . getSetting ( '1080pquality' ) == 'true' :
     o00ooO = i1i1I111iIi1 [ 'url' ]
     break
  else :
   o00ooO = i1i1IiIi1
 return o00ooO
def o0O0OO0o ( name , mu_playlist , queueVideo = None ) :
 iIO0O0Oooo0o = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if '$$LSPlayOnlyOne$$' in mu_playlist [ 0 ] :
  mu_playlist [ 0 ] = mu_playlist [ 0 ] . replace ( '$$LSPlayOnlyOne$$' , '' )
  import urlparse
  OOOoOo = [ ]
  OOoO0oo0O = 0
  o0o00OOo0 = xbmcgui . DialogProgress ( )
  o0o00OOo0 . create ( 'Progress' , 'Trying Multiple Links' )
  for III1ii1iII in mu_playlist :
   if 49 - 49: IIIiiIIii
   if '$nome=' in III1ii1iII :
    II1ii1ii11I1 = III1ii1iII . split ( '$nome=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    OOOoOo . append ( II1ii1ii11I1 )
    mu_playlist [ OOoO0oo0O ] = III1ii1iII . split ( '$nome=' ) [ 0 ] + ( '&regexs' + III1ii1iII . split ( '&regexs' ) [ 1 ] if '&regexs' in III1ii1iII else '' )
   else :
    II1ii1ii11I1 = urlparse . urlparse ( III1ii1iII ) . netloc
    if II1ii1ii11I1 == '' :
     OOOoOo . append ( name )
    else :
     OOOoOo . append ( II1ii1ii11I1 )
   i111IiI1I = OOoO0oo0O
   OOoO0oo0O += 1
   if 88 - 88: ooO00oOoo
   oOO = OOOoOo [ i111IiI1I ]
   if o0o00OOo0 . iscanceled ( ) : return
   o0o00OOo0 . update ( OOoO0oo0O / len ( mu_playlist ) * 100 , "" , "Link#%d" % ( OOoO0oo0O ) , oOO )
   print 'auto playnamexx' , oOO
   if "&mode=19" in mu_playlist [ i111IiI1I ] :
    oOoO00O0 = xbmcgui . ListItem ( oOO , iconImage = OOoOoo00Oo )
    oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : oOO } )
    oOoO00O0 . setProperty ( "IsPlayable" , "true" )
    ooooo0OoO0 = Ii1iI111II1I1 ( mu_playlist [ i111IiI1I ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    oOoO00O0 . setPath ( ooooo0OoO0 )
    ii1I111i1Ii = tryplay ( ooooo0OoO0 , oOoO00O0 )
   elif "$doregex" in mu_playlist [ i111IiI1I ] :
    OOOooO0OO0o = mu_playlist [ i111IiI1I ] . split ( '&regexs=' )
    if 10 - 10: oO - ii1IiI1i . OoooooooOO . i1iII1I1i1i1 . i1 * IiiIIiiI11
    ooOO00O00oo , iiiii1II = i1iiIiI1Ii1i ( OOOooO0OO0o [ 1 ] , OOOooO0OO0o [ 0 ] )
    OOOO = ooOO00O00oo . replace ( ';' , '' )
    oOoO00O0 = xbmcgui . ListItem ( oOO , iconImage = OOoOoo00Oo )
    oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : oOO } )
    oOoO00O0 . setProperty ( "IsPlayable" , "true" )
    oOoO00O0 . setPath ( OOOO )
    ii1I111i1Ii = tryplay ( OOOO , oOoO00O0 )
    if 94 - 94: OoooooooOO . i1iIIi1 + oO - OoOoOO00
   else :
    ooOO00O00oo = mu_playlist [ i111IiI1I ]
    ooOO00O00oo = ooOO00O00oo . split ( '&regexs=' ) [ 0 ]
    oOoO00O0 = xbmcgui . ListItem ( oOO , iconImage = OOoOoo00Oo )
    oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : oOO } )
    oOoO00O0 . setProperty ( "IsPlayable" , "true" )
    oOoO00O0 . setPath ( ooOO00O00oo )
    ii1I111i1Ii = tryplay ( ooOO00O00oo , oOoO00O0 )
    print 'played' , ii1I111i1Ii
   print 'played' , ii1I111i1Ii
   if ii1I111i1Ii : return
  return
 if I11iIi1I . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  OOOoOo = [ ]
  OOoO0oo0O = 0
  print mu_playlist
  for III1ii1iII in mu_playlist :
   print III1ii1iII
   if '$nome=' in III1ii1iII :
    II1ii1ii11I1 = III1ii1iII . split ( '$nome=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    OOOoOo . append ( II1ii1ii11I1 )
    mu_playlist [ OOoO0oo0O ] = III1ii1iII . split ( '$nome=' ) [ 0 ] + ( '&regexs' + III1ii1iII . split ( '&regexs' ) [ 1 ] if '&regexs' in III1ii1iII else '' )
   else :
    II1ii1ii11I1 = urlparse . urlparse ( III1ii1iII ) . netloc
    if II1ii1ii11I1 == '' :
     OOOoOo . append ( name )
    else :
     OOOoOo . append ( II1ii1ii11I1 )
     if 1 - 1: IIIiiIIii . O0
   OOoO0oo0O += 1
  oOOOOoOO0o = xbmcgui . Dialog ( )
  i111IiI1I = oOOOOoOO0o . select ( '[COLOR green][B]Brasil [/B][/COLOR][COLOR yellow][B]Full[/B][/COLOR] - Selecione uma Opcao:' , OOOoOo )
  if i111IiI1I >= 0 :
   oOO = OOOoOo [ i111IiI1I ]
   print 'playnamexx' , oOO
   if "&mode=19" in mu_playlist [ i111IiI1I ] :
    oOoO00O0 = xbmcgui . ListItem ( oOO , iconImage = OOoOoo00Oo )
    oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : oOO } )
    oOoO00O0 . setProperty ( "IsPlayable" , "true" )
    ooooo0OoO0 = Ii1iI111II1I1 ( mu_playlist [ i111IiI1I ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    oOoO00O0 . setPath ( ooooo0OoO0 )
    xbmc . Player ( ) . play ( ooooo0OoO0 , oOoO00O0 )
   elif "$doregex" in mu_playlist [ i111IiI1I ] :
    OOOooO0OO0o = mu_playlist [ i111IiI1I ] . split ( '&regexs=' )
    ooOO00O00oo , iiiii1II = i1iiIiI1Ii1i ( OOOooO0OO0o [ 1 ] , OOOooO0OO0o [ 0 ] )
    OOOO = ooOO00O00oo . replace ( ';' , '' )
    oOoO00O0 = xbmcgui . ListItem ( oOO , iconImage = OOoOoo00Oo )
    oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : oOO } )
    oOoO00O0 . setProperty ( "IsPlayable" , "true" )
    oOoO00O0 . setPath ( OOOO )
    xbmc . Player ( ) . play ( OOOO , oOoO00O0 )
    if 37 - 37: i1IIi - i1iII1I1i1i1 % OoooooooOO / i1iII1I1i1i1 % i1iIIi1
   else :
    ooOO00O00oo = mu_playlist [ i111IiI1I ]
    ooOO00O00oo = ooOO00O00oo . split ( '&regexs=' ) [ 0 ]
    oOoO00O0 = xbmcgui . ListItem ( oOO , iconImage = OOoOoo00Oo )
    oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : oOO } )
    oOoO00O0 . setProperty ( "IsPlayable" , "true" )
    oOoO00O0 . setPath ( ooOO00O00oo )
    xbmc . Player ( ) . play ( ooOO00O00oo , oOoO00O0 )
 elif not queueVideo :
  iIO0O0Oooo0o . clear ( )
  ii111iI1iIi1 = 0
  for III1ii1iII in mu_playlist :
   ii111iI1iIi1 += 1
   iiIiII11i1 = xbmcgui . ListItem ( '%s) %s' % ( str ( ii111iI1iIi1 ) , name ) )
   try :
    if "$doregex" in III1ii1iII :
     OOOooO0OO0o = III1ii1iII . split ( '&regexs=' )
     ooOO00O00oo , iiiii1II = i1iiIiI1Ii1i ( OOOooO0OO0o [ 1 ] , OOOooO0OO0o [ 0 ] )
    elif "&mode=19" in III1ii1iII :
     ooOO00O00oo = Ii1iI111II1I1 ( III1ii1iII . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if ooOO00O00oo :
     iIO0O0Oooo0o . add ( ooOO00O00oo , iiIiII11i1 )
    else :
     raise
   except Exception :
    iIO0O0Oooo0o . add ( III1ii1iII , iiIiII11i1 )
    pass
    if 93 - 93: ii1IiI1i % iIii1I11I1II1
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 90 - 90: OoOoOO00 - i1iII1I1i1i1 / oO / O0 / i1iIIII
  oOO00oO00O0OO = xbmcgui . ListItem ( name )
  iIO0O0Oooo0o . add ( mu_playlist , oOO00oO00O0OO )
  if 87 - 87: ii1IiI1i / oooOOOOO + iIii1I11I1II1
  if 93 - 93: iIii1I11I1II1 + O0OOo % i1iIIi1
def iii1IiI1I1 ( name , url ) :
 if I11iIi1I . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('BrasilFull','Escolha um local para salvar os arquivos.',15000," + o0oO0 + ")" )
  I11iIi1I . openSettings ( )
 iIIIiI = { 'url' : url , 'download_path' : I11iIi1I . getSetting ( 'save_location' ) }
 downloader . download ( name , iIIIiI )
 oOOOOoOO0o = xbmcgui . Dialog ( )
 I111IIiii1Ii = oOOOOoOO0o . yesno ( 'BrasilFull' , 'VocÃª deseja adicionar esse arquivo como fonte?' )
 if I111IIiii1Ii :
  I1II1III11iii ( os . path . join ( I11iIi1I . getSetting ( 'save_location' ) , name ) )
  if 64 - 64: i1iIIi1 / O0 * ii1IiI1i * i1iIIi1
  if 60 - 60: i1iIIII / i1IIi % ooO00oOoo / ooO00oOoo * ooO00oOoo . i11iIiiIii
def Ii1I ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False ) :
 if 99 - 99: ii1IiI1i
 oO00OoOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 oOoO00O0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO00O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 oOoO00O0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OoO = [ ]
  if showcontext == 'source' :
   if name in str ( o000o0o00o0Oo ) :
    OoO . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'download' :
   OoO . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   OoO . append ( ( 'Remove from Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 10 - 10: i1iIIII / i1iIIII * i11iIiiIii
  if not name in i1IIi11111i :
   OoO . append ( ( 'Add to Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOoO00O0 . addContextMenuItems ( OoO )
 OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO00OoOo , listitem = oOoO00O0 , isFolder = True )
 if 46 - 46: i1 * OOooo000oo0 % O0OOo + O0 * oooOOOOO
 return OO
def ii1I11i ( url , title , media_type = 'video' ) :
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 89 - 89: IiiIII111ii . oooOOOOO % OOooo000oo0 . OOooo000oo0 - OoooooooOO
   YDStreamExtractor . manageDownloads ( )
  else :
   oo0ooO0O0o = xbmc . Player ( ) . getPlayingFile ( )
   if 75 - 75: II111iiii + i1iII1I1i1i1
   oo0ooO0O0o = oo0ooO0O0o . split ( '|User-Agent=' ) [ 0 ]
   iiIiII11i1 = { 'url' : oo0ooO0O0o , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = iiIiII11i1 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 28 - 28: OoOoOO00
def Ii ( site_name , search_term = None ) :
 i1I1ii = ''
 if os . path . exists ( O0oo0OO0 ) == False or I11iIi1I . getSetting ( 'clearseachhistory' ) == 'true' :
  oo00OOoOoO00 ( O0oo0OO0 , '' )
  I11iIi1I . setSetting ( "clearseachhistory" , "false" )
 if site_name == 'history' :
  O0O0ooOOO = Ii11iI ( O0oo0OO0 )
  oOOo0O00o = re . compile ( '(.+?):(.*?)(?:\r|\n)' ) . findall ( O0O0ooOOO )
  if 49 - 49: i1iIIII . IIIiiIIii % O0OOo / oO
  for OOO00O , search_term in oOOo0O00o :
   if 'plugin://' in search_term :
    oooooo0O000o ( search_term , OOO00O , i1I1ii , '' , '' , '' , '' , '' , None , '' , total = int ( len ( oOOo0O00o ) ) )
   else :
    Ii1I ( OOO00O + ':' + search_term , OOO00O , 26 , o0oO0 , oo00 , '' , '' , '' , '' )
 if not search_term :
  iIi11Ii1 = xbmc . Keyboard ( '' , 'Enter Search Term' )
  iIi11Ii1 . doModal ( )
  if ( iIi11Ii1 . isConfirmed ( ) == False ) :
   return
  search_term = iIi11Ii1 . getText ( )
  if len ( search_term ) == 0 :
   return
 search_term = search_term . replace ( ' ' , '+' )
 search_term = search_term . encode ( 'utf-8' )
 if 'youtube' in site_name :
  import _ytplist
  if 95 - 95: O0 * ii1IiI1i * oooOOOOO . i1iIIi1 / iIii1I11I1II1
  I1IIi1I = { }
  I1IIi1I = _ytplist . YoUTube ( 'searchYT' , youtube = search_term , max_page = 4 , nosave = 'nosave' )
  oOooOOOoOo = len ( I1IIi1I )
  for ii111iI1iIi1 in I1IIi1I :
   try :
    OOO00O = I1IIi1I [ ii111iI1iIi1 ] [ 'title' ]
    i1IiIiiI = I1IIi1I [ ii111iI1iIi1 ] [ 'date' ]
    try :
     iIii1i1 = I1IIi1I [ ii111iI1iIi1 ] [ 'desc' ]
    except Exception :
     iIii1i1 = 'UNAVAIABLE'
     if 65 - 65: O0OOo + ooO00oOoo / i1iII1I1i1i1
    ooOO00O00oo = 'plugin://plugin.video.youtube/play/?video_id=' + I1IIi1I [ ii111iI1iIi1 ] [ 'url' ]
    i1I1ii = 'http://img.youtube.com/vi/' + I1IIi1I [ ii111iI1iIi1 ] [ 'url' ] + '/0.jpg'
    oooooo0O000o ( ooOO00O00oo , OOO00O , i1I1ii , '' , '' , '' , '' , '' , None , '' , oOooOOOoOo )
   except Exception :
    I1 ( 'This item is ignored::' )
  oo0oo = site_name + ':' + search_term + '\n'
  oo00OOoOoO00 ( os . path . join ( IiII , 'history' ) , oo0oo , append = True )
 elif 'dmotion' in site_name :
  IiIIi11i111 = "https://api.dailymotion.com"
  import _DMsearch
  oooo = str ( I11iIi1I . getSetting ( 'familyFilter' ) )
  _DMsearch . listVideos ( IiIIi11i111 + "/videos?fields=description,duration,id,owner.username,taken_time,thumbnail_large_url,title,views_total&search=" + search_term + "&sort=relevance&limit=100&family_filter=" + oooo + "&localization=en_EN&page=1" )
  if 27 - 27: i11iIiiIii - OoOoOO00
  oo0oo = site_name + ':' + search_term + '\n'
  oo00OOoOoO00 ( os . path . join ( IiII , 'history' ) , oo0oo , append = True )
 elif 'IMDBidplay' in site_name :
  IiIIi11i111 = "http://www.omdbapi.com/?t="
  ooOO00O00oo = IiIIi11i111 + search_term
  if 35 - 35: OoooooooOO - IiiIII111ii / i1
  I11iIi1II = dict ( { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; rv:33.0) Gecko/20100101 Firefox/33.0' , 'Referer' : 'http://joker.org/' , 'Accept-Encoding' : 'gzip, deflate' , 'Content-Type' : 'application/json;charset=utf-8' , 'Accept' : 'application/json, text/plain, */*' } )
  if 50 - 50: ii1IiI1i
  ooOOoO = requests . get ( ooOO00O00oo , headers = I11iIi1II )
  iIii1 = ooOOoO . json ( )
  i1i1Ii11Ii = iIii1 [ 'Response' ]
  if i1i1Ii11Ii == 'True' :
   O000oOo = iIii1 [ 'imdbID' ]
   OOO00O = iIii1 [ 'Title' ] + iIii1 [ 'Released' ]
   oOOOOoOO0o = xbmcgui . Dialog ( )
   I111IIiii1Ii = oOOOOoOO0o . yesno ( 'Check Movie Title' , 'PLAY :: %s ?' % OOO00O )
   if I111IIiii1Ii :
    ooOO00O00oo = 'plugin://plugin.video.quasar/movie/' + O000oOo + '/play'
    oo0oo = OOO00O + ':' + ooOO00O00oo + '\n'
    oo00OOoOoO00 ( O0oo0OO0 , oo0oo , append = True )
    return ooOO00O00oo
  else :
   xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,No IMDB match found ,7000," + o0oO0 + ")" )
   if 41 - 41: O0 + O0OOo . i1IIi - II111iiii * IIIiiIIii . i1
def oooO00Oo ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def ooO00o ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def o0o00O0oOooO0 ( s ) : return "" . join ( filter ( lambda o0oO0OO00ooOO : ord ( o0oO0OO00ooOO ) < 128 , s ) )
if 5 - 5: OoOoOO00 * ii1IiI1i - i11iIiiIii . i1iIIi1 / IiiIIiiI11
def III1iii1i1II ( command ) :
 iIii1 = ''
 try :
  iIii1 = xbmc . executeJSONRPC ( ooO00o ( command ) )
 except UnicodeEncodeError :
  iIii1 = xbmc . executeJSONRPC ( oooO00Oo ( command ) )
  if 87 - 87: i1iII1I1i1i1 + IIIiiIIii . IiiIIiiI11 - OoooooooOO
 return ooO00o ( iIii1 )
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
def iIiI1I1ii1I1 ( ) :
 O00oO = xbmc . getSkinDir ( )
 if O00oO == 'skin.confluence' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif O00oO == 'skin.aeon.nox' :
  xbmc . executebuiltin ( 'Container.SetViewMode(511)' )
 else :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 83 - 83: IIIiiIIii
def i1iiii ( url ) :
 OOOO0oOo00O = ooO00o ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}' ) % url
 if 32 - 32: oooOOOOO % oO - OoOoOO00
 oo0ooooo00o = json . loads ( III1iii1i1II ( OOOO0oOo00O ) )
 for III1ii1iII in oo0ooooo00o [ 'result' ] [ 'files' ] :
  url = III1ii1iII [ 'file' ]
  OOO00O = o0o00O0oOooO0 ( III1ii1iII [ 'label' ] )
  i1I1ii = o0o00O0oOooO0 ( III1ii1iII [ 'thumbnail' ] )
  try :
   i11Iiii = o0o00O0oOooO0 ( III1ii1iII [ 'fanart' ] )
  except Exception :
   i11Iiii = ''
  try :
   i1IiIiiI = III1ii1iII [ 'year' ]
  except Exception :
   i1IiIiiI = ''
  try :
   Oo = III1ii1iII [ 'episode' ]
   Ooi111i1iIi1 = III1ii1iII [ 'season' ]
   if Oo == - 1 or Ooi111i1iIi1 == - 1 :
    iIii1i1 = ''
   else :
    iIii1i1 = '[COLOR yellow] S' + str ( Ooi111i1iIi1 ) + '[/COLOR][COLOR hotpink] E' + str ( Oo ) + '[/COLOR]'
  except Exception :
   iIii1i1 = ''
  try :
   OoO0oO = III1ii1iII [ 'studio' ]
   if OoO0oO :
    iIii1i1 += '\n Studio:[COLOR steelblue] ' + OoO0oO [ 0 ] + '[/COLOR]'
  except Exception :
   OoO0oO = ''
   if 10 - 10: i1IIi . II111iiii / IIIiiIIii * i1iIIi1
  if III1ii1iII [ 'filetype' ] == 'file' :
   oooooo0O000o ( url , OOO00O , i1I1ii , i11Iiii , iIii1i1 , '' , i1IiIiiI , '' , None , '' , total = len ( oo0ooooo00o [ 'result' ] [ 'files' ] ) )
   if 10 - 10: i1iIIII - OOooo000oo0
  else :
   Ii1I ( OOO00O , url , 53 , i1I1ii , i11Iiii , iIii1i1 , '' , i1IiIiiI , '' )
   if 59 - 59: OoooooooOO * OOooo000oo0 + i1IIi
def oooooo0O000o ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" ) :
 OoO = [ ]
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 OO = True
 if 23 - 23: i1iIIi1
 if regexs :
  i11 = '17'
  if 56 - 56: OoOoOO00
  OoO . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif any ( x in url for x in IiII1IiiIiI1 ) and url . startswith ( 'http' ) :
  i11 = '19'
  if 12 - 12: OoOoOO00 - i1iIIi1
  OoO . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  i11 = '18'
  if 45 - 45: oooOOOOO / O0 / ii1IiI1i * i1iII1I1i1i1
  OoO . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if I11iIi1I . getSetting ( 'dlaudioonly' ) == 'true' :
   OoO . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'tbusca' ) or 'tbusca' in url :
  if 'Quasar' in I1i1iiI1 :
   url = 'plugin://plugin.video.quasar/search'
   i11 = '54'
 elif url . startswith ( 'magnet:?xt=' ) or '.torrent' in url :
  if 18 - 18: iIii1I11I1II1 + i1iII1I1i1i1 + iIii1I11I1II1 . ooO00oOoo + IiiIII111ii . i1iIIi1
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
   if 7 - 7: ooO00oOoo + iIii1I11I1II1 * i1iIIII * i1iIIII / II111iiii - oO
  if 'YATP' in I1i1iiI1 :
   url = 'plugin://plugin.video.yatp/?action=play&torrent=' + url
   i11 = '12'
  if 'KmediaTorrent' in I1i1iiI1 :
   url = 'plugin://plugin.video.kmediatorrent/play/' + url
   i11 = '12'
  if 'Quasar' in I1i1iiI1 :
   url = 'plugin://plugin.video.quasar/play?uri=' + url
   i11 = '12'
  if 'Pulsar' in I1i1iiI1 :
   url = 'plugin://plugin.video.pulsar/play?uri=' + url
   i11 = '12'
  if 'Torrenter' in I1i1iiI1 :
   url = 'plugin://plugin.video.torrenter/?action=playTorrent&url=' + url
   i11 = '12'
  if 'XBMCtorrent' in I1i1iiI1 :
   url = 'plugin://plugin.video.xbmctorrent/play/' + url
   i11 = '12'
 else :
  i11 = '12'
  if 65 - 65: O0OOo + ii1IiI1i + II111iiii
  OoO . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 oO00OoOo = sys . argv [ 0 ] + "?"
 oOOoo = False
 if 6 - 6: i1iII1I1i1i1
 if playlist :
  if I11iIi1I . getSetting ( 'add_playlist' ) == "false" :
   oO00OoOo += "url=" + urllib . quote_plus ( url ) + "&mode=" + i11
  else :
   oO00OoOo += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR steelblue] (' + str ( len ( playlist ) ) + ' Opções )[/COLOR]'
   oOOoo = True
 else :
  oO00OoOo += "url=" + urllib . quote_plus ( url ) + "&mode=" + i11
 if regexs :
  oO00OoOo += "&regexs=" + regexs
 if not setCookie == '' :
  oO00OoOo += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 98 - 98: OoooooooOO % O0 - O0
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 oOoO00O0 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oOoO00O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 oOoO00O0 . setProperty ( "Fanart_Image" , fanart )
 if 76 - 76: i1IIi % ii1IiI1i - OoOoOO00 / IIIiiIIii * i1iIIi1
 if ( not oOOoo ) and not any ( x in url for x in iIiiiI1IiI1I1 ) :
  if regexs :
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) :
    oOoO00O0 . setProperty ( 'IsPlayable' , 'true' )
  else :
   oOoO00O0 . setProperty ( 'IsPlayable' , 'true' )
 else :
  I1 ( 'NOT setting isplayable' + url )
  if 4 - 4: OOooo000oo0 * OOooo000oo0 / ii1IiI1i
 if showcontext :
  OoO = [ ]
  if showcontext == 'fav' :
   OoO . append (
 ( 'Remove from Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in i1IIi11111i :
   Ii1Ii1Ii1I1I = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   if playlist :
    Ii1Ii1Ii1I1I += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    Ii1Ii1Ii1I1I += "&regexs=" + regexs
   OoO . append ( ( 'Add to Add-on Favorites' , 'XBMC.RunPlugin(%s)' % Ii1Ii1Ii1I1I ) )
  oOoO00O0 . addContextMenuItems ( OoO )
  if 48 - 48: OOooo000oo0 - i1iIIi1 + OOooo000oo0 - OoOoOO00 * i11iIiiIii . IiiIIiiI11
 if not playlist is None :
  if I11iIi1I . getSetting ( 'add_playlist' ) == "false" :
   I1iIIIiI = name . split ( ') ' ) [ 1 ]
   OoiI1I1 = [
 ( 'Play ' + I1iIIIiI + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( I1iIIIiI ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   oOoO00O0 . addContextMenuItems ( OoiI1I1 )
 OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO00OoOo , listitem = oOoO00O0 , totalItems = total )
 return OO
 if 27 - 27: i1iIIi1 - OOooo000oo0 + IiiIIiiI11 - i1iII1I1i1i1 . OoOoOO00
def OOOOO0 ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  oOoO00O0 = xbmcgui . ListItem ( name , iconImage = iconimage )
  oOoO00O0 . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  oOoO00O0 . setProperty ( "IsPlayable" , "true" )
  oOoO00O0 . setPath ( str ( url ) )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoO00O0 )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 79 - 79: II111iiii - i1iIIi1 . i1IIi + O0 % O0 * OoOoOO00
def IiIIii1iII1II ( link ) :
 ooOO00O00oo = urllib . urlopen ( link )
 Ii1Ii1I = ooOO00O00oo . read ( )
 ooOO00O00oo . close ( )
 oOO0oo = Ii1Ii1I . split ( "Jetzt" )
 Oo00O0OO = oOO0oo [ 1 ] . split ( 'programm/detail.php?const_id=' )
 oOOOoo0o = Oo00O0OO [ 1 ] . split ( '<br /><a href="/' )
 iiiI1IiIIii = oOOOoo0o [ 0 ] [ 40 : len ( oOOOoo0o [ 0 ] ) ]
 IIIIiiiIi11Ii1iI = Oo00O0OO [ 2 ] . split ( "</a></p></div>" )
 OOOo00 = IIIIiiiIi11Ii1iI [ 0 ] [ 17 : len ( IIIIiiiIi11Ii1iI [ 0 ] ) ]
 OOOo00 = OOOo00 . encode ( 'utf-8' )
 return "  - " + OOOo00 + " - " + iiiI1IiIIii
 if 15 - 15: i1iIIII
 if 94 - 94: IiiIII111ii % II111iiii * i1IIi * iIii1I11I1II1
def o0O ( url , regex ) :
 iIii1 = ii11iIi1I ( url )
 try :
  ii111iI1iIi1 = re . findall ( regex , iIii1 ) [ 0 ]
  return ii111iI1iIi1
 except :
  I1 ( 'regex failed' )
  I1 ( regex )
  return
  if 81 - 81: OOooo000oo0 - i1iIIII
  if 24 - 24: OoooooooOO . i1 * II111iiii
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 59 - 59: IiiIII111ii + i1 / i1iII1I1i1i1
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 97 - 97: OOooo000oo0 * IiiIIiiI11 % i1iIIi1 . IiiIIiiI11 - IiiIII111ii - i1iII1I1i1i1
iIIIiI = IIi1iI ( )
if 79 - 79: OoOoOO00 - i1iIIi1
ooOO00O00oo = None
OOO00O = None
i11 = None
iIO0O0Oooo0o = None
OOoOoo00Oo = None
i11Iiii = oo00
iIO0O0Oooo0o = None
I11 = None
oo00oOO000oO0 = None
if 39 - 39: i1iIIi1 + O0 / i1IIi % oooOOOOO / O0OOo * oooOOOOO
try :
 ooOO00O00oo = urllib . unquote_plus ( iIIIiI [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 OOO00O = urllib . unquote_plus ( iIIIiI [ "name" ] )
except :
 pass
try :
 OOoOoo00Oo = urllib . unquote_plus ( iIIIiI [ "iconimage" ] )
except :
 pass
try :
 i11Iiii = urllib . unquote_plus ( iIIIiI [ "fanart" ] )
except :
 pass
try :
 i11 = int ( iIIIiI [ "mode" ] )
except :
 pass
try :
 iIO0O0Oooo0o = eval ( urllib . unquote_plus ( iIIIiI [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 I11 = int ( iIIIiI [ "fav_mode" ] )
except :
 pass
try :
 oo00oOO000oO0 = iIIIiI [ "regexs" ]
except :
 pass
 if 77 - 77: oooOOOOO . IiiIII111ii % ii1IiI1i
I1 ( "Mode: " + str ( i11 ) )
if not ooOO00O00oo is None :
 I1 ( "URL: " + str ( ooOO00O00oo . encode ( 'utf-8' ) ) )
I1 ( "Name: " + str ( OOO00O ) )
if 42 - 42: oooOOOOO % IiiIIiiI11 % IIIiiIIii % O0OOo + i1iIIII % ii1IiI1i
if i11 == None :
 I1 ( "Index" )
 OooOoO0Oo ( )
 if 3 - 3: O0OOo
elif i11 == 1 :
 I1 ( "getData" )
 iiIIiIiIi ( ooOO00O00oo , i11Iiii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 64 - 64: i1 . OoOoOO00 - OoooooooOO . i1iIIi1 - IiiIIiiI11
elif i11 == 2 :
 I1 ( "getChannelItems" )
 ii1I1 ( OOO00O , ooOO00O00oo , i11Iiii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 77 - 77: oO % ii1IiI1i / II111iiii % IiiIIiiI11 % OoooooooOO % i1
elif i11 == 3 :
 I1 ( "getSubChannelItems" )
 ooO0O00Oo0o ( OOO00O , ooOO00O00oo , i11Iiii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 19 - 19: oooOOOOO * IiiIII111ii / O0OOo * IiiIII111ii - OoooooooOO * i1iIIII
elif i11 == 4 :
 I1 ( "getFavorites" )
 I1I11ii ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 17 - 17: II111iiii + OOooo000oo0 . IiiIII111ii
elif i11 == 5 :
 I1 ( "addFavorite" )
 try :
  OOO00O = OOO00O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OOO00O = OOO00O . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOOo ( OOO00O , ooOO00O00oo , OOoOoo00Oo , i11Iiii , I11 )
 if 12 - 12: IiiIII111ii + i1iII1I1i1i1 + i1iIIII . oooOOOOO / oO
elif i11 == 6 :
 I1 ( "rmFavorite" )
 try :
  OOO00O = OOO00O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OOO00O = OOO00O . split ( '  - ' ) [ 0 ]
 except :
  pass
 OoO0oO00o ( OOO00O )
 if 29 - 29: oooOOOOO . i1iIIi1 - II111iiii
elif i11 == 7 :
 I1 ( "addSource" )
 I1II1III11iii ( ooOO00O00oo )
 if 68 - 68: iIii1I11I1II1 + II111iiii / O0OOo
elif i11 == 8 :
 I1 ( "rmSource" )
 oO000Oo000 ( OOO00O )
 if 91 - 91: ii1IiI1i % iIii1I11I1II1 . OoOoOO00
elif i11 == 9 :
 I1 ( "download_file" )
 iii1IiI1I1 ( OOO00O , ooOO00O00oo )
 if 70 - 70: i1iIIII % II111iiii % O0 . i1IIi / IiiIII111ii
elif i11 == 10 :
 I1 ( "getCommunitySources" )
 IIi1i11111 ( )
 if 100 - 100: ooO00oOoo * i11iIiiIii % O0OOo / OOooo000oo0 / i1iIIi1 + ooO00oOoo
elif i11 == 11 :
 I1 ( "addSource" )
 I1II1III11iii ( ooOO00O00oo )
 if 59 - 59: IiiIII111ii - oooOOOOO
elif i11 == 12 :
 I1 ( "setResolvedUrl" )
 if not ooOO00O00oo . startswith ( "plugin://plugin" ) or not any ( x in ooOO00O00oo for x in iIiiiI1IiI1I1 ) :
  ii111iI1iIi1 = xbmcgui . ListItem ( path = ooOO00O00oo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii111iI1iIi1 )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + ooOO00O00oo + ')' )
  if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
  if 5 - 5: oooOOOOO
elif i11 == 13 :
 I1 ( "play_playlist" )
 o0O0OO0o ( OOO00O , iIO0O0Oooo0o )
 if 84 - 84: II111iiii * O0OOo * II111iiii % oooOOOOO / OoOoOO00
elif i11 == 14 :
 I1 ( "get_xml_database" )
 oOOOOo0 ( ooOO00O00oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 100 - 100: oooOOOOO . oO - iIii1I11I1II1 . i11iIiiIii / II111iiii
elif i11 == 15 :
 I1 ( "browse_xml_database" )
 oOOOOo0 ( ooOO00O00oo , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 71 - 71: IiiIII111ii * OOooo000oo0 . i1iIIII
elif i11 == 16 :
 I1 ( "browse_community" )
 IIi1i11111 ( True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 49 - 49: oooOOOOO * O0 . oooOOOOO
elif i11 == 17 :
 I1 ( "getRegexParsed" )
 ooOO00O00oo , iiiii1II = i1iiIiI1Ii1i ( oo00oOO000oO0 , ooOO00O00oo )
 if ooOO00O00oo :
  OOOOO0 ( ooOO00O00oo , OOO00O , OOoOoo00Oo , iiiii1II )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(BrasilFull ,Failed to extract regex. - " + "this" + ",4000," + o0oO0 + ")" )
elif i11 == 18 :
 I1 ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(BrasilFull,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 oooOo0OOOoo0 = youtubedl . single_YD ( ooOO00O00oo )
 OOOOO0 ( oooOo0OOOoo0 , OOO00O , OOoOoo00Oo )
elif i11 == 19 :
 I1 ( "Genesiscommonresolvers" )
 OOOOO0 ( Ii1iI111II1I1 ( ooOO00O00oo ) , OOO00O , OOoOoo00Oo , True )
 if 19 - 19: II111iiii - oooOOOOO
elif i11 == 21 :
 I1 ( "download current file using youtube-dl service" )
 ii1I11i ( '' , OOO00O , 'video' )
elif i11 == 23 :
 I1 ( "get info then download" )
 ii1I11i ( ooOO00O00oo , OOO00O , 'video' )
elif i11 == 24 :
 I1 ( "Audio only youtube download" )
 ii1I11i ( ooOO00O00oo , OOO00O , 'audio' )
elif i11 == 25 :
 I1 ( "YouTube/DMotion" )
 Ii ( ooOO00O00oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i11 == 26 :
 I1 ( "YouTube/DMotion From Search History" )
 OOO00O = OOO00O . split ( ':' )
 Ii ( ooOO00O00oo , search_term = OOO00O [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i11 == 27 :
 I1 ( "Using IMDB id to play in Pulsar" )
 OOOOo000o00OO = Ii ( ooOO00O00oo )
 xbmc . Player ( ) . play ( OOOOo000o00OO )
elif i11 == 30 :
 i111iIi1i1II1 ( OOO00O , ooOO00O00oo , OOoOoo00Oo , i11Iiii )
 if 96 - 96: O0 . i1iII1I1i1i1 % i1iIIi1 + i11iIiiIii - i1iII1I1i1i1 * i1iIIi1
elif i11 == 40 :
 i11III1111iIi ( )
 iIiI1I1ii1I1 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 33 - 33: i1iIIi1 % i1IIi - O0OOo . O0 / O0
elif i11 == 53 :
 I1 ( "Requesting JSON-RPC Items" )
 i1iiii ( ooOO00O00oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 96 - 96: OoooooooOO + oooOOOOO * O0
elif i11 == 54 :
 I1 ( "Burst" )
 xbmc . executebuiltin ( 'XBMC.RunPlugin(' + ooOO00O00oo + ')' )
 if 86 - 86: oO
elif i11 == 55 :
 I1 ( "getSearchData" )
 iIii1 = None
 if oo00oOO000oO0 and len ( oo00oOO000oO0 ) > 0 :
  iIii1 , iiiii1II = i1iiIiI1Ii1i ( oo00oOO000oO0 , ooOO00O00oo )
  if 29 - 29: iIii1I11I1II1 - i1 + OoOoOO00 % iIii1I11I1II1 % i1iII1I1i1i1
  if 84 - 84: oooOOOOO + ooO00oOoo + oO + IiiIIiiI11
  if iIii1 . startswith ( 'http' ) or iIii1 . startswith ( 'smb' ) or iIii1 . startswith ( 'nfs' ) or iIii1 . startswith ( '/' ) :
   ooOO00O00oo = iIii1
   iIii1 = None
   if 62 - 62: i11iIiiIii + ii1IiI1i + i1IIi
 ooOOOoOooOoO ( ooOO00O00oo , i11Iiii , iIii1 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 69 - 69: ii1IiI1i
 if 63 - 63: i1 / ii1IiI1i * iIii1I11I1II1 . IiiIII111ii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
