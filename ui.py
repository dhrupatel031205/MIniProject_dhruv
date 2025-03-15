# this is the task A

from reactpy import html, component, run

@component
def home():
    return html.div(
        {
            'style': {
                'background': 'linear-gradient(100deg, black, cyan, black, cyan, black)',
                'textAlign': 'center',
                'borderRadius': '10px',
                'padding': '70px',
                'fontFamily': 'monospace',
            }
        },
        html.img(
            {
                'style': {
                    'height': '300px',
                    'width': '500px',
                    'borderRadius': '50px',
                    'border': '4px solid cyan',
                },
                'src': 'https://images.pexels.com/photos/9783353/pexels-photo-9783353.jpeg?auto=compress&cs=tinysrgb&w=600'
            }
        ),
        html.h1(
            {'style': {
                'color': 'white',
                'fontFamily': 'monospace',
                'fontSize': '45px',
                'padding': '20px',
                'textShadow': '0 0 20px cyan, 0 0 30px cyan'
            }},
            'Welcome to the Text Zone and automation'
        ),
        html.h2(
            {'style': {
                'color': 'white',
                'margin': '50px',
                'padding': '0 100px',
                'textShadow': '0 0 20px cyan, 0 0 30px cyan'
            }},
            'You can get the text from the different ways and one funny automation is also waiting for u...'
        ),
        
        html.div(
            {'style': {'display': 'flex', 'justifyContent': 'center', 'gap': '20px', 'marginTop': '20px'}},
            html.a(
                {
                    'href': 'http://localhost:7860',
                    'target': '_blank',
                    'style': {
                        'color': 'black',
                        'textDecoration': 'none',
                        'fontSize': '20px',
                        'padding': '10px 20px',
                        'background': 'cyan',
                        'borderRadius': '20px',
                        'border': '5px solid white'
                    }
                },
                'Explore Our Bots'
            ),
            html.a(
                {
                    'href': 'http://localhost:8501',
                    'target': '_blank',
                    'style': {
                        'color': 'black',
                        'textDecoration': 'none',
                        'fontSize': '20px',
                        'padding': '10px 20px',
                        'background': 'cyan',
                        'borderRadius': '20px',
                        'border': '5px solid white'
                    }
                },
                'Automation'
            ),
            
        )
    )

run(home)

