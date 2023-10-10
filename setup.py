from distutils.core import setup
setup(
    name = 'rey',         
    packages = ['rey'],   
    version = '0.1',      
    license='MIT',    
    description = 'An API wrapper designed to simplify the process of integrating Line Messaging API',
    author = 'TheGenocide',
    author_email = 'luke.genesis.hyder@gmail.com',
    url = 'https://github.com/TheGenocides/rey',
    download_url = 'https://github.com/TheGenocides/rey/archive/refs/tags/first-release.tar.gz',
    keywords = ['line-bot', 'apiwrapper', 'line', 'api'],
    install_requires=[
        'aiohttp'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11.5'

    ],
)