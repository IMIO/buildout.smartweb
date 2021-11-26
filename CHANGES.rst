1.0a5 (unreleased)
------------------

- Nothing changed yet.


1.0a4-quick (2021-11-26)
------------------------

- imio.smartweb.core 1.0a16

    - Add profile to handle bundles last_compilation dates
      [laulaz]

    - Add new css styles
      [thomlamb]

    - Udpate data for content items view
      [thomlamb]

    - Refactor css className
      [thomlamb]

    - Add moment js to parsed date
      [thomlamb]

    - New build of react vue
      [thomlamb]

    - Disallow hiding title on a collapsable section
      [laulaz]

    - Fix bootstrap classes for table batches
      [laulaz]

    - Can define specific events to get (instead of all events from an agenda)
      [boulch]

    - Use Swiper instead of Bootstrap carousel
      [thomlamb, laulaz]


- imio.smartweb.policy 1.0a7

    - Restore Default workflow on Link type
      [laulaz]

    - Change 'en-un-click' to ifind folder and add iam folder with some links + upgrade steps.
      [boulch]


- imio.smartweb.locales 1.0a8

    - Add missing translations
      [laulaz]


1.0a3 (2021-11-24)
------------------

- imio.smartweb.policy 1.0a6

    - Add upgrade to restrict collections views (will always be faceted layouts)
      [laulaz]


- imio.smartweb.locales 1.0a7

    - Add missing translations
      [laulaz]


- imio.smartweb.common 1.0a4

    - Add utility to get a vocabulary
      [boulch]


- imio.smartweb.core 1.0a15

    - Allow to override / limit icons TTW (portal_resources)
      [laulaz]

    - React Routge improvement
      [thomlamb]

    - Refactor css className
      [thomlamb]

    - fix a problem or react call the endpoint several times
      [thomlamb]

    - New react build
      [thomlamb]

    - Allow from 1 to 8 links per batch in links section
      [laulaz]

    - Add more icons and use English names and titles for icons
      [laulaz]

    - Change HTML field help to describe how to use it
      [laulaz]

    - Hide icons profile from installer
      [laulaz]

    - Fix banner not displaying in minisites
      [laulaz]

    - Remove "Hide/Display banner from this item" link on banner in Preview mode
      [laulaz]


- imio.smartweb.core 1.0a14
  
    - Force endpoints returning values as JSON 
      [laulaz]
    
    - Update news root and refactor code 
      [thomlamb]
    
    - prettify code and delete useless state 
      [thomlamb]
    
    - Add responsible 16:9 ratio on embed videos 
      [laulaz]
    
    - Add collapsable option for sections (click on section title opens section body) 
      [laulaz]
    
    - Add SVG icon option for block links, with icon resolver and basic icons set 
      [laulaz]
    
    - Cleanup useless code 
      [laulaz]


- imio.smartweb.core 1.0a13
  
    - Change url for fetch search filters data.
      [thomlamb]


1.0a2 (2021-11-16)
------------------

- imio.smartweb.core 1.0a12

    - Add blocks / list faceted layouts and (automatic) criteria configuration for
      collections
      [laulaz]

    - Add new fields on rest views (event types, contact categories) to filter
      results and adapt endpoints
      [boulch]

    - Refactor folder views html code to simplify it & make it more efficient (no
      more waking up of objects)
      [laulaz]

    - Remove e_guichet action (replaced by generic account action) and add css class
      on all header actions
      [laulaz]

    - Add text on search link for acessibility
      [laulaz]

    - Adapt `@search` endpoint to be context based for SolR searches
      [mpeeters]

    - Change max results logic for a number of batches (collection / events / news)
      [laulaz]

    - Add React search view
      [tlambert]

    - Fix SearchableText indexing for links / video sections (new) descriptions
      [laulaz]

    - Define cropping scales for all contents / fields
      [laulaz]

    - Add/fix bootstrap classes on table / carousel views for batches
      [laulaz]

    - Change image scales for listing (liste) / blocks (vignette) view and table
      view (liste / vignette), depending on batch size
      [laulaz]

    - Change image scale (affiche) for sections background images
      [laulaz]

    - Use background images (instead of `<img>`) in table template
      [laulaz]

    - Add (rich) description on Video section
      [laulaz]

    - Change some fields titles
      [laulaz]

    - Fix @@search view (use ours instead of collective.solr)
      [laulaz]


- imio.smartweb.policy 1.0a5

    - Add cropping support on File content type
      [laulaz]


- imio.smartweb.common 1.0a3

    - Avoid traceback if configure_faceted is called on non-configured type (ex: on
      default collections at Plone install)
      [laulaz]


- imio.smartweb.locales 1.0a6

    - Add missing translations
      [laulaz]


1.0a1 (2021-11-05)
------------------

- Initial release
  [boulch]
