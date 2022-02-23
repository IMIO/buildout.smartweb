1.0-quick (2022-02-23)
----------------------

- imio.smartweb.core 1.0

    - Add description in sendinblue section
      [boulch]

    - Add conditions on faceted and folder view (with images).
      When we select one of this view and if a content hasn't image we display a no-image class
      [boulch]

    - Fix css for news items
      [thomlamb]

    - Change event contact icon
      [thomlamb]

    - Override social tags generation to get scaled images instead of full size.
      We didn't override syndication to avoid any side effects in RSS / Atom
      [laulaz]

- imio.smartweb.policy 1.0

    - Install and set collective autoscaling with some default values
      [boulch]

- imio.smartweb.locales 1.0a16

    - Fix translation
      [laulaz]

- imio.smartweb.core 1.0a43

    - Limitate usage of site search settings to current website search
      [mpeeters]

- imio.smartweb.common 1.0a11

    - Load Analytics via JS call to avoid non-privacy aware caching
      [laulaz]
    
    - Change privacy views permissions to zope.Public 
      [laulaz]

- imio.smartweb.core 1.0a42

    - Fix bad html link for news items
      [thomlamb]

    - Fix removed section subscriber. if we removed a folder, pages with sections stayed in catalog
      [boulch]

- imio.smartweb.core 1.0a41

    - Fix loadmore react views
      [thomlamb]

    - Update Axios module to 26.0
      [thomlamb]

    - Add AbortController to prevent unnecessary requests
      [thomlamb]

    - Use `use_site_search_settings` parameters by default to inherit query parameters from site search settings
      for `@search` endpoint
      [mpeeters]


1.0a19-quick (2022-02-14)
-------------------------

- imio.smartweb.core 1.0a40

    - Fix bug with react import img
      [thomlamb]


1.0a18-quick (2022-02-14)
-------------------------

- imio.smartweb.core 1.0a39

    - Fix missing value for placeholder 
      [thomlamb]


1.0a17-quick (2022-02-14)
-------------------------

- imio.smartweb.core 1.0a38

    - Fix condition to display search items img
      [thomlamb]

- imio.smartweb.core 1.0a37

    - Fix problem with react event map
      [thomlamb]

    - Add background image for result search items
      [thomlamb]

    - Refactor all js indent
      [thomlamb]

    - Add placeholder class on contact logo & leadimage when they are empty
      [laulaz]

    - Change/fix max number (30) of possible sections in pages before paging
      [boulch]

    - Add new div with a nb-items-batch-[N] class
      to ease stylizing multi items templates (table, carousel)
      [boulch]

    - Fix bad css value
      [thomlamb]

- Fix some auto-checkout to revisions instead of branches
  [boulch]


1.0a16-quick (2022-02-11)
-------------------------

- imio.smartweb.core 1.0a36

    - Update e-guichet icon file & add new shopping icon
      [laulaz]

    - Change default value for batch size in files section
      [laulaz]

    - Improve css
      [thomlamb]

    - Avoid fetching contact from authentic source multiple times on the same view
      [laulaz]

- imio.smartweb.policy 1.0a17

    - Send BAN request after a messageviewlet creation / modification / removal
      [laulaz]

- imio.smartweb.locales 1.0a15

    - Add new icons translations (e-guichet & shopping)
      [laulaz]


1.0a15 (2022-02-10)
-------------------

- imio.smartweb.core 1.0a35

    - Use css class & background style also on footers sections
      [laulaz]

    - Correction of spelling mistakes
      [thomlamb]

    - Get events with new event_dates index
      [laulaz]

    - Change footer markup to have only one row
      [laulaz]

    - Add new e-guichet icon
      [laulaz]

    - Remove GDPR link from footer (it is already in colophon)
      [laulaz]

    - Restore removed class to help styling carousel by batch size
      [laulaz]

- imio.smartweb.common 1.0a10

    - Hide ical import related actions
      [laulaz]


1.0a14-quick (2022-02-10)
-------------------------

- imio.smartweb.policy 1.0a16

    - Add imio.prometheus dependency to get metrics view.
      [bsuttor]

- Up RelStorage to 3.4.5
  [laulaz] 


1.0a13 (2022-02-09)
-------------------

- imio.smartweb.core 1.0a34

    - Fix missing permissions to add footer
      [laulaz] 

    - Fix default item view for a collection when anonymous
      [laulaz] 

    - Fix double escaped navigation items in quick accesses
      See https://github.com/plone/plone.app.layout/issues/280
      [laulaz] 


1.0a12-quick (2022-02-08)
-------------------------

- imio.smartweb.core 1.0a33

    - Fix search axios to not fetch with no filter set
      [thomlamb]

- imio.smartweb.core 1.0a32

    - Change Youtube & Parking base icons, and add Twitter
      [laulaz] 

    - Add id on sections containers to ease styling
      [laulaz]

    - Be sure to reindex the container (& change modification date for cachinig) when
      a page has been modified
      [laulaz]

    - Reorder SectionContact template + modify some translations
      [boulch]

    - Fix generated url for search results
      [thomlamb]

    - Unauthorize to add imio.smartweb.SectionSendinblue on a Page but authorize it on PortalPage.
      [boulch]

    - Include source item url for `@search` service results
      [mpeeters]

    - Enforce using SolR for `@search` service
      [mpeeters]

    - Fix translation domain for event macro
      [laulaz]

- imio.smartweb.locales 1.0a14

    - Add social network translation
      [laulaz]


1.0a11-quick (2022-02-04)
-------------------------

- imio.smartweb.policy 1.0a15

    - Activate plone.app.caching.moderateCaching.lastModified
      [sverbois, laulaz]

    - Use auto-checkout for collective.z3cform.select2 (Plone 6)
      [laulaz]

- imio.smartweb.locales 1.0a13

    - Add event dates related translations
      [laulaz]

- imio.smartweb.core 1.0a31

    - Disable sticky map on mobile
      [thomlamb]
  
    - Refactor : Displaying dates from section event is now in a macro to have more html flexibility
      [boulch, laulaz]

- imio.smartweb.locales 1.0a12

    - Add e_guichet view and taxonomies instance behaviors translations
      [laulaz]

- imio.smartweb.policy 1.0a14

    - Add collective.z3cform.select2 as a dependency
      [boulch]

- imio.smartweb.core 1.0a30

    - Allow to set instance behaviors on page or on procedure objects
      [boulch, laulaz]

    - Improve react vue for mobile
      [thomlamb]

    - Change static js and css for mobile responsive search
      [thomlamb]

    - Simplifying faceted macros
      [boulch]

- imio.smartweb.core 1.0a29

    - Fix error in navigation when filtering on workflow state
      [laulaz]

    - Adapt faceted macros to discern section video and other contents. Fix video redirect link thanks to css.
      [boulch]

- imio.smartweb.policy 1.0a13

    - Upgrade step : Reload portal types to add imio.smartweb.listing behavior on links
      [boulch]

    - Patch ALL caching operations to add Cache-Control header even when
      intercepting a 304 NOT MODIFIED
      [laulaz]

    - Update buildout to use Plone 6.0.0a3 packages versions
      [boulch]

- Update Sendinblue packages to use v3 API key
  [laulaz]

- imio.smartweb.common 1.0a9

    - Update buildout to use Plone 6.0.0a3 packages versions
      [boulch]

    - Remove unneeded override: it has been included in plone.app.z3c.form
      See https://github.com/plone/plone.app.z3cform/issues/138
      [laulaz]

- imio.smarweb.core 1.0a28

    - Fix navigation in subsites after navtree_depth property removal
      See https://github.com/plone/plone.app.layout/commit/7e2178d2ae11780d9211c71d8c97e4f81cd27620
      [laulaz]

    - Update buildout to use Plone 6.0.0a3 packages versions
      [boulch]

    - Allow collections as folders default view
      [laulaz]

    - Add links on folder titles in navigation
      [laulaz]

    - Fix double escaped navigation items
      See https://github.com/plone/plone.app.layout/issues/280
      [laulaz]

- Update Dockerfile to match Plone6 buildout
  PIP=21.3.1, ZC_BUILDOUT=3.0.0rc1, SETUPTOOLS=59.6.0, PLONE_MAJOR=6.0, PLONE_VERSION=6.0.0a3
  [boulch]

- By default, comment debug-products to avoid many pdb with solr
  [boulch]

- imio.smartweb.core 1.0a27

    - Add upgrade step to check contact itinerary if address is in visible blocks
      [boulch]

    - Contact itinerary go out of contact address. Itinerary is displaying thanks to a new visible_blocks option value
      [boulch]

    - Improve and resolv bug in load more in react vue
      [thomlamb]

    - Add new Sendinblue newsletter subscription section
      [laulaz]

    - disabling filter resets on search load (important, to settle a conflict with other react views)
      [thomlamb]

    - Precision so that the css of the search is unique to itself
      [thomlamb]

- imio.smartweb.policy 1.0a12

    - Patch terse caching operation to add Cache-Control header even when
      intercepting a 304 NOT MODIFIED
      [laulaz]

    - Fix client caching value in terseCaching (was different in upgrade step)
      [laulaz]

- imio.smartweb.locales 1.0a11

    - Add Sendinblue related translations
      [laulaz]

    - Change translation for short name
      [laulaz]

- Update buildout to use Plone 6.0.0a3 packages versions
  [boulch]

- Set zodb-cache-size and zeo-client-cache-size from env variables.
  [bsuttor]

- imio.smartweb.policy 1.0a11

    - Fix Plone translations override
      [laulaz]

- imio.smartweb.core 1.0a26

    - Disable input search limit
      [thomlamb]

    - Small correction of rendered data in views and scss
      [thomlamb]

    - Fix local search when no text in input
      [thomlamb]

- imio.smartweb.core 1.0a25

    - Avoid page reload after gallery spolight close
      [laulaz]

    - Fix default value for search filters
      [thomlamb]

    - Fix open_in_new_tab option for BlockLinks
      [laulaz]

    - Allow some python modules in restricted python (Usefull for collective.themefragments modules)
      [boulch]

    - Add offcanvas bootstrap component in a viewlet and inherit from search browserview
      [boulch, thomlamb]

    - Always keep (empty) placeholder div in carousel/table templates even if item has no image
      [laulaz]

    - Fix traceback when section selection target has no description
      [laulaz]

- Add products : collective.themefragments = 2.12
  [boulch]


1.0a10 (2022-01-26)
-------------------

- imio.smartweb.core 1.0a24

    - New react build
      [thomlamb]

    - Adding loadmore for react vue
      [thomlamb]

    - Improved query for search filters
      [thomlamb]

    - Link changes for search results.
      [thomlamb]

    - Update generated url for search items to match with react vue.
      [thomlamb]

    - Fix street address formatting (number after street name)
      [laulaz]

    - Add new css class in text section to stylize figure based on their size
      [boulch]

    - Add @@is_eguichet_aware view to get e-guichet configuration/connexion status
      [boulch]

- Update Dockerfile to match Plone6 buildout
  PIP=21.0.1, ZC_BUILDOUT=3.0.0b2, SETUPTOOLS=54.0.0A, PLONE_MAJOR=6.0, PLONE_VERSION=6.0.0a2
  [boulch]

- Use released version for pas.plugins.authomatic
  [laulaz]

- imio.gdpr 1.2.1

    - Add icons for control panel settings (Plone5 / 6 size)
      [boulch]

    - Override a plone.app.registry template to have structured (html) description
      [boulch]

- imio.smartweb.locales 1.0a10

    - Add / change cookies related translations
      [laulaz]

    - Update buildout to use Plone 6.0.0a2 packages versions
      [laulaz]

- imio.smartweb.common 1.0a8

    - Change colophon copyright position
      [laulaz]

    - Change cookies viewlet / overlay logic. We now show (simplified) overlay only
      to see detailed options about cookies because viewlet allows to Accept / Refuse
      all cookies directly
      [laulaz]

    - Add Cookies preferences link in colophon
      [laulaz]

    - Change some cookies-related texts
      [laulaz]

    - Fix iframes transform with existing classes or when there are several iframes
      [laulaz]

- iaweb.privacy 1.0a2

    - SUP-21477: Change default cookies texts
      [laulaz]

- imio.smartweb.policy 1.0a10

    - Update buildout to use Plone 6.0.0a2 released version
      [laulaz]

    - Get some missing upgrades steps from plone6 dev to plone6 released
      [boulch]

    - Load/register caching configuration + move upgrades steps in an upgrades folder.
      [boulch]

    - Remove client caching in terseCaching
      [sverbois]

- imio.smartweb.core 1.0a23

    - Update buildout to use Plone 6.0.0a2 released version
      [laulaz]

    - Avoid traceback when trying to display an empty schedule
      [laulaz]

    - Add breadcrumb to some select box in smartweb settings.
      [boulch]

- imio.smartweb.common 1.0a7

    - Update buildout to use Plone 6.0.0a2 released version
      [laulaz]

    - Remove portal messages from cookies settings overlay
      [laulaz]

- Use released version for collective.anysurfer & pas.plugins.imio
  [laulaz]

- Update buildout & packages to use Plone 6.0.0a2 released version
  [laulaz]


1.0a9-quick (2022-01-14)
------------------------

- imio.smartweb.common 1.0a6

    - Add cookies opt-in support for analytics and iframes
      [laulaz]

    - Override colophon viewlet to display legal mention, accessibility info and
      copyright links (dependency on imio.gdpr)
      [laulaz]


- imio.smartweb.core 1.0a22

    - Add dynamic style for leaflet. + general styles
      [thomlamb]


- imio.smartweb.locales 1.0a9

    - Add missing translations
      [laulaz]


- imio.smartweb.policy 1.0a9

    - Restore Plone colophon viewlet in footer
      [laulaz]


- Use released version for collective.complexrecordsproxy
  [laulaz]


- Switch collective.anysurfer & collective.autopublishing to master
  [boulch, laulaz]


1.0a8 (2021-12-16)
------------------

- imio.smartweb.common 1.0a5

    - Fix vocabulary term translation (missing lang)
      [laulaz]


- imio.smartweb.policy 1.0a8

    - Add caching configuration
      [sverbois]


- imio.smartweb.core 1.0a21

    - Adding load more button for react list element
      [thomlamb]

    - Improvement js of the Schedule popup
      [thomlamb]

    - Change image size scales (that were too small)
      [laulaz]

    - Add events dates in events section
      [laulaz]

    - Make HTML section folderish (can contain Images and Files)
      [laulaz]

    - Add description on HTML section
      [laulaz]

    - Section contact : Share address into 3 parts (street, entity, country) and display these parts into span
      [boulch]

    - Javascript refactoring
      [thomlamb]

    - Distribution of css in the global file
      [thomlamb]

    - Add global style for all component.
      [thomlamb]

    - Add removeAccents js for string url
      [thomlamb]

    - Add "with-background" css class on sections that have a background image
      [laulaz]

    - Add items category in news / events section
      [laulaz]

    - Add news items publication date in news section
      [laulaz]

    - Add option to display items descriptions in news / events / selection sections
      [laulaz]


1.0a7 (2021-12-08)
------------------

- Set threads to 2 to decrease connections to postgres cluster #WEB-3578.
  [bsuttor]


1.0a6 (2021-12-06)
------------------

- imio.smartweb.core 1.0a20

    - Change markup and css classes for carousel / table templates
      [laulaz]

    - Set SolR connections for external sources
      [mpeeters]

    - Add routing for react search vue.
      [thomamb]


1.0a5 (2021-12-01)
------------------

- imio.smartweb.core 1.0a19

    - Avoid an unwanted behavior with path index combined with SolR and virtual host
      [mpeeters]


- imio.smartweb.core 1.0a18

    - Avoid batching on vocabularies : contact categories and entity events
      [laulaz]

    - Add plone.shortname behavior on all sections
      [laulaz]

    - Restrict search inside minisites
      [laulaz]

    - Fix footer viewlet markup to be included in Plone footer
      [laulaz]

    - Add faceted layout class to body if a faceted layout is define.
      [boulch]


- imio.smartweb.core 1.0a17

    - Move background_style (img background) out of sections (section-container div) and put it in pages view (sortable-section div). This simplifying css styling.
      [boulch]

    - Split section macros to "manage macros" to manage sections and "title macros" to print sections title + add default Plone "container" css class.
      [boulch]

    - Change generated url for the news and event sections for compatibility with react router
      [thomamb]


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
