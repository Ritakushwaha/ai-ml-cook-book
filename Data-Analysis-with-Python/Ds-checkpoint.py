{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'SOP_Tech_Assessment.xlsx'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-773ddcea9cf6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_excel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'SOP_Tech_Assessment.xlsx'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msheet_name\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'Raw data'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\util\\_decorators.py\u001b[0m in \u001b[0;36mwrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    206\u001b[0m                 \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    207\u001b[0m                     \u001b[0mkwargs\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnew_arg_name\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnew_arg_value\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 208\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    209\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    210\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\io\\excel\\_base.py\u001b[0m in \u001b[0;36mread_excel\u001b[1;34m(io, sheet_name, header, names, index_col, usecols, squeeze, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, keep_default_na, verbose, parse_dates, date_parser, thousands, comment, skip_footer, skipfooter, convert_float, mangle_dupe_cols, **kwds)\u001b[0m\n\u001b[0;32m    308\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    309\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mio\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mExcelFile\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 310\u001b[1;33m         \u001b[0mio\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mExcelFile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mio\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mengine\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    311\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mio\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    312\u001b[0m         raise ValueError(\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\io\\excel\\_base.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, io, engine)\u001b[0m\n\u001b[0;32m    817\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_io\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_stringify_path\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mio\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    818\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 819\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_reader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engines\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_io\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    820\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    821\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__fspath__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\io\\excel\\_xlrd.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, filepath_or_buffer)\u001b[0m\n\u001b[0;32m     19\u001b[0m         \u001b[0merr_msg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"Install xlrd >= 1.0.0 for Excel support\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m         \u001b[0mimport_optional_dependency\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"xlrd\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mextra\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merr_msg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m         \u001b[0msuper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\io\\excel\\_base.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, filepath_or_buffer)\u001b[0m\n\u001b[0;32m    357\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbook\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_workbook\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    358\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 359\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbook\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_workbook\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    360\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    361\u001b[0m             raise ValueError(\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\io\\excel\\_xlrd.py\u001b[0m in \u001b[0;36mload_workbook\u001b[1;34m(self, filepath_or_buffer)\u001b[0m\n\u001b[0;32m     34\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mopen_workbook\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfile_contents\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 36\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mopen_workbook\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     37\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     38\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\xlrd\\__init__.py\u001b[0m in \u001b[0;36mopen_workbook\u001b[1;34m(filename, logfile, verbosity, use_mmap, file_contents, encoding_override, formatting_info, on_demand, ragged_rows)\u001b[0m\n\u001b[0;32m    109\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    110\u001b[0m         \u001b[0mfilename\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexpanduser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 111\u001b[1;33m         \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"rb\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    112\u001b[0m             \u001b[0mpeek\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpeeksz\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    113\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mpeek\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34mb\"PK\\x03\\x04\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;31m# a ZIP file\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'SOP_Tech_Assessment.xlsx'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_excel('SOP_Tech_Assessment.xlsx', sheet_name='Raw data')\n",
    "print(df.head(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
