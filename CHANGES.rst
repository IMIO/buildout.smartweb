1.0a3 (unreleased)
------------------

- imio.smartweb.common 1.0a4

    - Add utility to get a vocabulary
      [boulch]

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
