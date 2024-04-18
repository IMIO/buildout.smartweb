1.2.14 (unreleased)
-------------------

- imio.smartweb.core 1.2.44

    - WEB-4099 : Fix select name
      [boulch]

- imio.smartweb.core 1.2.43

    - WEB-4099 : Resize sections in front-end thanks to htmx / jquery
      [boulch]

    - WEB-4098 : Add affiche scale for section on table view display and one element by lot
      [thomlamb]

    - WEB-4098 : Add new profile for imio.smartweb.orientation to section files
      [thomlamb]

    - SUP-35100 : Fix sitemap.xml.gz generation. When a "main" rest view was removed, continue to build sitemap for others rest views
      [boulch]


1.2.13 (2024-04-14)
-------------------

- imio.smartweb.core 1.2.42

    - SUP-36564 : Fix arcgis external content plugin
      [boulch]

- Migrate to Plone 6.0.9
  [boulch]


1.2.12 (2024-04-04)
-------------------

- imio.smartweb.core 1.2.41

    - Set higher timeout because retrieving some datas can take some time
      [boulch]

- imio.smartweb.locales 1.1.15

    - Add missing fr, nl, de translations
      [boulch]

- imio.smartweb.core 1.2.40

    - MWEBPM-9 : Add container_uid in rest views to retrieve agenda id/title or news folder id/title
      [boulch]

    - MWEBPM-9 : Retrieve agenda id/title or news folder id/title and display it in "common templates" table
      [boulch]

- imio.smartweb.locales 1.1.14

    - Add missing fr, nl, de translations
      [boulch]

    - Update translations
      [boulch]

- imio.smartweb.locales 1.1.13

    - Add missing fr, nl, de translations
      [boulch]

    - Update translations
      [boulch]

- imio.smartweb.core 1.2.39

    - MWEBPM-9 : Retrieve agenda id/title or news folder id/title and display it in "common templates" carousel
      [boulch]

    - MWEBPM-8 : Add "min" or "max" to queries depending to "only past events"
      [thomlamb]

    - MWEBPM-8 : Add field to manage "only past events" rest view
      [boulch]

- imio.smartweb.core 1.2.38

    - Fix React build
      [thomlamb]

    - Fix spelling mistake and react compilation
      [boulch]

- imio.smartweb.core 1.2.37

    - Add new plugin in external content section / refactor some code in external content section
      [boulch]

    - Add figcaption content in alt attribute for images in section text
      [thomlamb]


1.2.11 (2024-03-05)
-------------------

- imio.smartweb.core 1.2.36

    - WEB-4072, WEB-4073 : Enable solr.fields behavior on some content types
      [remdub]

    - WEB-4001 : Refactoring the generation of sitemap.xml.gz
      [boulch]

- imio.smartweb.core 1.2.35

    - WEB-4006 : Exclude some content types from search results
      [remdub]

- collective.solr 9.3.0

    - Add support of https connections
      [remdub]

    - Add french locales
      [remdub]

- collective.solr 9.2.3

    - Add upgrade step for missing stopwords registry entries
      [remdub]

- WEB-3862 : eea.facetednavigation 16.2
  [boulch]

- imio.smartweb.core 1.2.34

    - MWEBRCHA-13 : Add content rules to notify reviewers (Install via validation profile)
      [laulaz]

    - MWEBRCHA-13 : Fix plone versioning (Work on SectionText / Remove from SectionHTML)
      [boulch]


1.2.10 (2024-02-12)
-------------------

- imio.smartweb.core 1.2.33

    - WEB-4067 : Override plone.app.content.browser.vocabulary.VocabularyView to provide filtering items to AjaxSelectFieldWidget
      [boulch]

    - WEB-4001 : Override sitemap.xml.gz to improve SEO with react views
      [boulch]

    - Change datePicker date format.
      [thomlamb]

    - Add class on section text if there is collapsable
      [thomlamb]

    - WEB-4056 : Refactoring: Removed sha256 encoding (no longer needed)
      [boulch]

    - WEB-3966: Add close navigation menu on focusout to make it more accessible
      [thomlamb]

- imio.smartweb.common 1.2.9

    - WEB-4064 : Reindex SolR because of changes in schema
      [remdub]

- WEB-4064 : Fix : remove copyfields on solr schema
  to avoid loosing SearchableText on an element when updating its parent
  [remdub]


1.2.9 (2024-02-05)
------------------

- imio.smartweb.core 1.2.32

    - Fix : Could not adapt (..interfaces.ITranslationManager) in single-language website when we set language param in url view
      [boulch]

    - Fix : rest_view_obj can be None if react view was removed
      [boulch]

    - Fix: bad condition to display search items number of results
      [thomlamb]

- imio.smartweb.common 1.2.8

    - Fix skip content sr-only
      [thomlamb]

- imio.smartweb.policy 1.2.4

    - Make content types translatable (with `plone.translatable` behavior) in
      multilingual profile.
      [laulaz]

- imio.smartweb.core 1.2.31

    - Add React Context to manage global language
      [thomlamb]

    - WEB-4063 : Create some views that redirect to main rest (directory, agenda, news) views (thank to registered uid) for e-guichet
      [boulch]

    - SUP-34498 : Fix url construction to fix 404 on external tab click on React items
      [thomlamb]

- imio.smartweb.core 1.2.30

    - Quick fix : move date queries in inital component to avoid bad url
      [thomlamb]


1.2.8-quick (2024-01-30)
------------------------

- imio.smartweb.core 1.2.30

    - Quick fix : move date queries in inital component to avoid bad url
      [thomlamb]


1.2.7-quick (2024-01-30)
------------------------

- imio.smartweb.core 1.2.29

    - Quick fix : effective date can be a str type. So the news sections were broken
      [boulch]


1.2.6 (2024-01-29)
------------------

- imio.smartweb.core 1.2.28

    - WEB-3802 : translate datepicker
      [thomlamb]

    - WEB-3802 : add nl traduction for React view.
      [thomlamb]

    - WEB-3802 : Fix datePicker filtre to no load on first date change
      [thomlamb]

- imio.smartweb.locales 1.1.12

    - Add missing translations
      [boulch]

    - Update translations
      [boulch]

    - WEB-4049 : Add missing german / dutch translations
      [boulch]

- imio.smartweb.core 1.2.27

    - WEB-3802 : Adding scss styles for new period filter
      [thomlamb]

    - WEB-3802 : Adding missing traduction for React view.
      [thomlamb]

    - WEB-4029 : Fix issue "invalid date" with pat-display-time and DateTime Zope/Plone format (with Firefox!)
      [boulch]

- imio.smartweb.core 1.2.26

    - WEB-3802 : Fix Axios Serializer to fix key in object request.
      [thomlamb]

- imio.smartweb.core 1.2.25

    - WEB-3802 : Adding perido filter in event React view
      [thomlamb]

- imio.smartweb.core 1.2.24

    - WEB-3802 : Get dates range for events in REST views. Coming from React.
      [boulch]

    - WEB-4050 : Fix : Loosing related_contacts ordering when changing any attributes in section
      [boulch]

    - WEB-4007 : Add Schedule in contact React view
      [thomlamb]

- imio.smartweb.policy 1.2.3

    - WEB-4046 : Add "Skip to content" viewlet in portal top
      [laulaz]

- imio.smartweb.common 1.2.7

    - WEB-4046 : Add css for "Skip to content"
      [thomlamb]

    - WEB-4046 : Add "Skip to content" link for a11y
      [laulaz]

    - WEB-4048 : Put focus on cookies accept button for a11y
      [laulaz]

- imio.smarteb.locales 1.1.11

    - WEB-4049 : Add missing german / dutch translations
      [boulch]

- imio.smartweb.core 1.2.23

    - WEB-4041 : Handle new "carre" scale
      [boulch]

- imio.smartweb.common 1.2.6

    - WEB-4041 : Add new "carre" scale
      [boulch]

- imio.smartweb.core 1.2.22

    - Refactor : Move ContactProperties (to build readable schedule) to imio.smartweb.common
      [boulch]

- imio.smartweb.common 1.2.5

    - WEB-4007 : Get ContactProperties out of imio.smartweb.core to also use it in imio.directory.core and 
      simplifying formated schedule displaying in REACT directory view
      [boulch]

    - WEB-4029 : File and Image content types don't have WF so we set effective date equal to created date
      [boulch]


1.2.5 (2023-12-18)
------------------

- imio.smartweb.core 1.2.21

    - WEB-3992 : Fix svg to have base color. Add class for icon in table template
      [thomlamb]

    - SUP-34061 : Fix React Gallery img scales
      [thomlamb]


1.2.4 (2023-12-11)
------------------

- DEVOPS-37 : force upgrade steps on promote
  [remdub,bsuttor]

- imio.smartweb.core 1.2.20

    - WEB-3783 : Update viewlet to set og:tags in rest views
      [boulch]

    - (Re)Activate external section
      [boulch]

- imio.smartweb.common 1.2.4

    - WEB-3783 : Rebuild url with request.form datas (usefull with react views)
      [boulch]

- imio.smartweb.locales 1.1.10

    - Add missing translations (plausible/statistics)
      [boulch]

    - Update translations
      [boulch]

- imio.smartweb.core 1.2.19

    - WEB-4022 : Fix : Compiled edit.js
      [boulch]

    - WEB-4022 : Fix : bad char in actions.xml (setup/upgrade step)
      [boulch]

- WEB-4028 : Restore `fix-geosearch` fork of `plone.formwidget.geolocation`
  We must wait for https://github.com/Patternslib/pat-leaflet/pull/36

- imio.smartweb.core 1.2.18

    - WEB-4022 : Create a new action menu with an utils view that redirect to stats (browser)view
      [boulch]

    - Change HashRouter to BrowserRouter in React & fix related URLs
      [thomlamb, laulaz]

    - WEB-3783 : Add new header viewlet to manage og:tags in REACT views
      [boulch]

- imio.smartweb.core 1.2.17

    - Refactor / optimize React code and upgrade packages
      [thomlamb]

- imio.smartweb.core 1.2.16

    - Handle single item json responses in request forwarders
      [laulaz]

- imio.smartweb.core 1.2.15

    - Handle empty responses in request forwarders
      [laulaz]

- imio.smartweb.core 1.2.14

    - Fix parameters in `POST` / `PATCH` / `DELETE` requests
      [laulaz]

- imio.smartweb.core 1.2.13

    - Use json for request forwarders body
      [laulaz, boulch]

- imio.smartweb.core 1.2.12

    - Deactivate Plone protect / Add token for queries
      [laulaz, boulch]

    - Handle PATCH & DELETE in request forwarders
      [laulaz]

    - Fix smartweb url and fix metadatas if missing fullobject
      [boulch]

- imio.smartweb.core 1.2.11

    - Add Smartweb related URLs in forwarded json responses
      [laulaz]

    - Transform requests forwarders into REST API Services
      [laulaz]

- imio.smartweb.core 1.2.10

    - Add RequestForwarder views
      [laulaz, boulch]


1.2.3 (2023-11-24)
------------------

- imio.smartweb.core 1.2.9

    - WEB-4021 : Fix lead image displaying with files section
      [boulch]


1.2.2-quick (2023-11-23)
------------------------

- Release to force new docker tag / deploy after incomplete build
  [laulaz]


1.2.1-quick (2023-11-23)
------------------------

- Fix use of bool env vars in `collective.solr`
  [remdub]

- imio.smartweb.core 1.2.8

    - Fix (lead) image sizes URLs for text section & migrate old values
      [boulch, laulaz]


1.2 (2023-11-22)
----------------

- imio.smartweb.core 1.2.7

    - Fix image scales URLs for gallery view thumbnails
      [laulaz]

    - WEB-3992 : Uncheck icon when clincking on checked icon (in edit form of imio.smartweb.BlockLink)
      [boulch]

- imio.smartweb.core 1.2.6

    - Fix tests after scales dimensions change
      [laulaz]

- imio.smartweb.policy 1.2.2

    - Improve collective autoscaling compression quality Also fix missing autoscaling settings for new instances
      [laulaz]

- imio.smartweb.common 1.2.3

    - Improve image compression quality
      [laulaz]

    - Change portrait scales dimensions
      [laulaz]

- imio.smartweb.core 1.2.5

    - Rebuild React to fix js errors
      [thomlamb]

    - WEB-4017 : Add Number 2 for items per batch
      [thomlamb]

    - Fix last upgrade steps: when run from command line, we need to adopt admin user to find private objects
      [laulaz]

    - Fix wrong type name in imio.smartweb.CirkwiView type profile
      [laulaz]

    - WEB-4014 : Display "websites" urls instead of labels (facebook, website, instagram, ...)
      [boulch]

    - WEB-4012 : Restored filter on related contacts field
      [boulch]

- imio.smartweb.common 1.2.2

    - Fix missing values for facilities lists (causing `None` in REST views filters)
      See https://github.com/collective/collective.solr/issues/366
      [laulaz]

    - Fix last upgrade steps: when run from command line, we need to adopt admin
      user to find private objects
      [laulaz]

    - WEB-4003 : Fix missing TextField mimetypes
      [laulaz]

- imio.smartweb.locales 1.1.9

    - WEB-4018 : Add missing French translations (new termes in directory vocabulary)
      [boulch]

- Add "run" script to clear and rebuild instances
  [boulch]

- Use released version of `plone.formwidget.geolocation`
  [laulaz]

- imio.smartweb.core 1.2.4

    - Handle image orientation on faceted map layout
      [laulaz]

    - Remove unused Photo Gallery from collections layouts
      [laulaz]

- Develop collective.solr to implement https connection DEVOPS-3
  [remdub]

- imio.smartweb.policy 1.2.1

    - Restore removed behaviors on Collection type
      [laulaz]

- imio.smartweb.common 1.2.1

    - SUP-33128 : Fix eea.facetednavigation : Hide items with 0 results
      [boulch, laz]

    - Refactor less and js compilation + Add compilations files
      [boulch]

- imio.smartweb.core 1.2.3

    - Migrate deprecated image scales from Section Contact / Gallery
      [laulaz]

    - Migrate "Is in portrait mode" option to orientation behavior for Section Contact
      [laulaz]

    - Handle image orientation on Collection & Foler types
      [laulaz]

    - Remove unused `gallery_view.pt` template
      [laulaz]

    - Change order of orientation options (default first)
      [laulaz]

    - Handle orientation in REST views images & fix galleries
      [laulaz]

    - Change default orientation to landscape
      [laulaz]

- imio.smartweb.core 1.2.2

    - WEB-3985 : Fix condition to load image or logo in contact view
      [thomlamb]

    - WEB-3985 : Fix logo scale URL (no orientation there) for Directory view
      [laulaz]

    - WEB-3985 : Fix React build
      [thomlamb]

- imio.smartweb.core 1.2.1

    - WEB-3985 : Fix traceback when cropping scale information is not present on image change
      [laulaz]

- imio.smartweb.core 1.2

    - WEB-3985 : New portrait / paysage scales & logic.
      We have re-defined the scales & sizes used in smartweb.
      We let the user crop only 2 big portrait / paysage scales and make the calculation behind the scenes for all
      other smaller scales.
      We also fixed the cropping information clearing on images changes.
      A new orientation behavior allow the editor to choose with type of image he wants.
      [boulch, laulaz]

    - Fix css for Event content view
      [thomlamb]

- imio.smartweb.common 1.2

    - WEB-3985 : New portrait / paysage scales & logic.
      We have re-defined the scales & sizes used in smartweb.
      We let the user crop only 2 big portrait / paysage scales and make the calculation behind the scenes for all
      other smaller scales.
      We also fixed the cropping information clearing on images changes.
      [boulch, laulaz]

- imio.smartweb.policy 1.2

    - WEB-3985 : Add orientation behavior on Collection type
      [boulch, laulaz]

- imio.smartweb.locales 1.1.8

    - Add missing French translations
      [laulaz]


1.1.15 (2023-10-24)
-------------------

- imio.smartweb.locales 1.1.7

    - Add missing French translations
      [boulch]

    - Update translations
      [boulch]

- imio.smartweb.core 1.1.30

    - Adaptation of react to show or hide the map
      [thomlamb]

    - WEB-3999 : Keep order of contacts in its view through manualy sorted related_contacts in edit form
      [boulch]

- imio.smartweb.core 1.1.29

    - SUP-32814 : Add new external content plugins : GiveADayPlugin
      see : https://github.com/IMIO/imio.smartweb.core/commit/a4dfca2
      [boulch]

    - WEB-4000 : Add display_map Bool field on directory and events views
      [boulch]

- imio.smartweb.core 1.1.28

    - WEB-3803 : Add upgrade step : collective.pivot.Family content type can be add in an imio.smartweb.Folder
      [boulch]

    - WEB-3998 : Set requests timeout to 8'' when we populate RemoteContacts vocabulary
      [boulch]

- imio.smartweb.policy 1.1.6

    - WEB-3803 : Monkey patch imio/collective.pivot post_install method to create an imio.smartweb.Folder
      to store defaults collective.pivot.Family contents
      [boulch]

- collective.pivot 1.0b2

    - Fix translation function
      [boulch]
    
    - Fix post_install when the targeted site not allow default Folder on plonesite root
      [boulch]


1.1.14 (2023-10-11)
-------------------

- imio.smartweb.core 1.1.27

    - Add <div> in view_argis.pt template to fix map displaying
      [thomlamb, jhero]


1.1.13 (2023-10-10)
-------------------

- imio.smartweb.locales 1.1.6

    - Add missing French translations (external content section and contact section)
      [boulch]

- imio.smartweb.core 1.1.26

    - Add missing upgrade step to add leadimage behavior on external content section
      [boulch]

    - Fix some translations in external content plugins
      [boulch]

- imio.smartweb.core 1.1.25

    - SUP-32169 : Add new external content plugins : ArcgisPlugin
      [boulch]


1.1.12 (2023-10-09)
-------------------

- imio.smartweb.policy 1.1.5

    - Remove deprecated overrides because we removed picture managing out of Tiny
      [boulch]

- imio.smartweb.core 1.1.24

    - WEB-3986 : Fix : email must be open thank to "mailto:" tag instead of "tel:"
      [boulch]

    - WEB-3984 : Remove deprecated cropping annotations on banner
      [boulch, laulaz]

    - WEB-3984 : Don't get banner scale anymore. Get full banner image directly
      [boulch, laulaz]

    - WEB-3984 : Remove banner field from cropping editor
      [laulaz]

- imio.smartweb.core 1.1.23

    - WEB-3983 : Fix contacts bootstrap grid
      [boulch]

    - WEB-3980 : Fix help and authentic sources menus double displaying in folder_contents view
      [boulch]

    - fix calculating image size on loading (add async in useEffect)
      [thomlamb]

    - WEB-3981 : Add Cognitoforms as an external section
      [boulch]

    - WEB-3932 : Transform contact section to contactS section
      [laulaz, boulch]


1.1.11 (2023-08-31)
-------------------

- pas.plugins.imio 2.0.9

    - Fix login could be id of user.
      [bsuttor]

    - Fix byte convertion error on python3.
      [bsuttor]


1.1.10-quick (2023-08-31)
-------------------------

- Pinned elder 2.0.7 version of pas.plugins.imio to test in staging (2.0.8 have some issues)
  [boulch]


1.1.9 (2023-08-29)
------------------

- imio.smartweb.core 1.1.22

    - Add smartweb content types icons (Message, MessagesConfig)
      [boulch]

    - Delete useless css for edition
      [thomlamb]
  
- imio.smartweb.core 1.1.21

    - Add smartweb content types icons
      [laulaz, boulch]

    - Show help & authentic sources menus only if product is installed
      [laulaz, boulch]

    - Update compiled resources to fix help menu
      [boulch]

    - Refactor Plausible
      [remdub]

- imio.smartweb.locales 1.1.5

    - Add missing translations
      [boulch]

- imio.smartweb.common 1.1.9

    - WEB-3974 : Add new registry key (imio.smartweb.common.log) to activate logging in smartweb / auth sources products
      [boulch]

    - Fix AttributeError in case of instance behaviors attributes that are not on all objects
      [boulch]

- imio.smartweb.core 1.1.20

    - Fix display of hours on events react view
      [thomlamb]

    - Refactor React contact view
      [thomlamb]

    - Refactor section text : image_size field is no more required because field is now hidden!
      [boulch]

    - WEB-3957 : Add new "Please help!" menu in Plone toolbar
      [boulch]

    - Display logo if no image in react contact card.
      Display blurry background if image is in portrait
      [thomlamb]

    - Fix of the calculation of the batch zise, ​​addition instead of concatenation
      [thomlamb]

    - WEB-3972 : Add "elloha" plugin in external content section
      [boulch]

- WEB-3781 : Upgrade `pas.plugins.imio` to fix issue with admin user
  [laulaz]

- imio.smartweb.common 1.1.8

    - WEB-3960 : Clean unhautorized xml chars out of text when added or modified contents Temporary patch.
      Waiting for this fix : plone/plone.app.z3cform#167
      [boulch]

    - WEB-3955 : Authentic sources : Crop view on Image type should not return scales
      [boulch]

- imio.smartweb.core 1.1.19

    - WEB-3956 : Update folder modification date when its layout changed to fix cache
      [boulch]

    - WEB-3934 : Hide image_size field
      [boulch]

    - WEB-3953 : Remove cropping from background_image field
      [boulch]

    - WEB-3952 : Disable image cropping on section text
      [laulaz, boulch]

    - Make "Image cropping" link conditional
      [laulaz]

    - Disable image cropping on Slide content type
      [laulaz]

    - Fix condition for image placeholder on React vue
      [thomlamb]

- imio.smartweb.core 1.1.18

    - Removal of unnecessary css in sections contact and gallery
      [thomlamb]

    - Add new browserview for Plausible
      [remdub, boulch]

    - Change some icons : SectionHTML and SectionExternalContent
      [boulch]

    - MWEBTUBA : Add new section : imio.smartweb.SectionExternalContent (Manage embeded contents)
      [boulch]


1.1.8 (2023-05-31)
------------------

- imio.smartweb.core 1.1.17

    - New React build
      [thomlamb]

    - Use hash in gallery images URL for directory, events and news rest views
      (based on modification date) to allow strong caching.
      [boulch, laulaz]


1.1.7 (2023-05-30)
------------------

- imio.smartweb.policy 1.1.4

    - Migrate to Plone 6.0.4
      [boulch]

    - Migrate to Plone 6.0.2
      [boulch]

    - WEB-3763 : Add new permission to manage configlets in control panel
      [boulch]

- imio.smartweb.locales 1.1.4

    - Add missing French translation (folder_contents properties)
      [laulaz]

    - Migrate to Plone 6.0.4
      [boulch]

- imio.smartweb.core 1.1.16

    - Fix faceted map size after page loading.
      [thomlamb]

    - Adapt `@search` endpoint to handle multilingual
      [mpeeters]

- imio.smartweb.core 1.1.15

    - Fixed console error following unnecessary loading of js for swiper
      [thomlamb]

    - Avoid image cropping for banner scale (will have infinite height)
      [laulaz]

    - Cleanup folder_contents properties & add warning about Sections
      [laulaz]

    - Store hash in an annotation to refresh "dynamic" sections
      [boulch, laulaz]

    - WEB-3868 : Remove useless code (included in Plone 6.0.4) See plone/plone.base#37
      [laulaz]

    - Migrate to Plone 6.0.4
      [boulch]

    - Update static icon for better css implements
      [thomlamb]

    - SUP-30074 : Fix broken RelationValue "AttributeError: 'NoneType' object has no attribute 'UID'
      [boulch]

- imio.smartweb.common 1.1.7

    - Change banner scale to have infinite height
      [laulaz]

    - Migrate to Plone 6.0.4
      [boulch]

- Rollback to Zope 5.8 for now because of a bug in POST requests with gunicorn
  [boulch]

- WEB-3781 : Add autopublish script
  [remdub]

- Migrate to Plone 6.0.4
  [boulch]


1.1.6 (2023-04-25)
------------------

- imio.smartweb.core 1.1.14

    - Fix image display condition
      [thomlamb]

    - Fix json attributes to get the scaling pictures of news
      [boulch]

- imio.smartweb.core 1.1.13

    - compile resources
      [boulch]

- imio.smartweb.common 1.1.6

    - Don't use image_scales metadata anymore (Fix faceted)
      [boulch, laulaz]

    - Update object modification date if cropping was removed/updated
      [boulch, laulaz]

- imio.smartweb.core 1.1.12

    - WEB-3868 : Forbid creating content with same id as a parent field
      [laulaz]

    - Don't use image_scales metadata anymore to get images scales URLs because we
      had problems with cropped scales (they were not indexed).
      We now use a hash in URL (based on modification date) to allow strong caching.
      See collective/plone.app.imagecropping#129
      [laulaz, boulch]

- imio.smartweb.core 1.1.11

    - WEB-3913 : Leadimages should not appear on rest views
      [boulch]


1.1.5 (2023-04-02)
------------------

- imio.smartweb.core 1.1.10

    - WEB-3901 : Get fullsize picture if scale is not present (section collection)
      [boulch]

    - WEB-3908 : Call new @events endpoint to get events occurrences
      [boulch]


1.1.4-quick (2023-03-20)
------------------------

- Push images to prod registry.
  [bsuttor]



1.1.3 (2023-03-19)
------------------

- imio.smartweb.core 1.1.9

    - WEB-3898 : Prevent error (error while rendering imio.smartweb.banner) if a content has his id = "banner"
      [boulch]

- imio.smartweb.core 1.1.8

    - WEB-3888 : We overrided link_input template widget to allow any link format in external tab (without browser blocking)
      [boulch]

    - WEB-3769 : Get fullsize picture if scale is not present (ex: picture too small)
      [boulch]

    - SUP-27477 : Fix internal link in herobanner
      [boulch]

- imio.smartweb.locales 1.1.3

    - Add missing French translations (Cirkwi & image dimensions warning)
      [laulaz]

    - Migrate to Plone 6.0.2
      [boulch]

- imio.smartweb.common 1.1.5

    - WEB-3862 : Patch (Remove select2) eea.facetednavigation jquery 
      [laulaz, boulch]

- imio.smartweb.common 1.1.4

    - Allow to add portal messages when content images are too small for cropping. This can be done dynamically on a view call with a single line of code: show_warning_for_scales(self.context, self.request)
      [laulaz]

    - Migrate to Plone 6.0.2
      [boulch]
    
- Upgrade collective.solr to `9.1.1` to include the latest fix for image_scales metadata
  [mpeeters]


1.1.2-quick (2023-03-08)
------------------------

- Develop collective.solr to fix an issue with image_scales metadata
  [mpeeters]


1.1.1 (2023-03-07)
------------------

- imio.smartweb.core 1.1.7

    - Improved react views to better match bootstrap media queries and fix no wrap buttons
      [thomlamb]

    - Fix no display img in news view
      [thomlamb]

    - Migrate to Plone 6.0.2
      [boulch]

    - WEB-3865 : Ordering news section and events section in their views thanks to a manualy order in their widgets
      [boulch]

    - Avoid auto-appending new lines to Datagrid fields when clicked
      [laulaz]

    - Fix annuaire, agenda, news sections with current language
      [boulch]

- Migrate to Plone 6.0.2
  [boulch]


1.1.0 (2023-02-22)
------------------

- imio.smartweb.core 1.1.6

    - WEB-3863 : Fix some dates displaying
      [boulch]

    - WEB-3858 : Fix displaying of authentic sources menu
      [boulch]

- imio.smartweb.locales 1.1.2

    - WEB-3848 : Add missing translations
      [boulch]

- imio.smartweb.common 1.1.3
  
    - WEB-3852 : Fix atom/syndication registry keys
      [boulch]

- Remove hack for overview-controlpanel from Dockerfile.
  [bsuttor]


1.1 (2023-02-20)
----------------

- imio.smartweb.locales 1.1.1

    - Add some new French translations (Cirkwi)
      [boulch]

- imio.smartweb.core 1.1.5

    - Delete lorem in React vue
      [thomlamb]

    - Fixed accessibility nav attribute
      [thomlamb]

    - Fixed faceted map
      [boulch]

    - WEB-3837 : Can define specific news to get (instead of all news from news folders)
      [boulch]

    - Adding display block on active dropdown
      [thomlamb]

    - Fix traduction ID for React
      [thomlamb]  

- imio.smartweb.policy 1.1.3

    - WEB-3820 : Added collective.geotransform but we don't deploy it automaticaly
      [boulch]

    - WEB-3833 : Hide plone.app.multilingual in control panel installable products
      [boulch]

- plone.formwidget.geolocation > fix-geosearch

    - Fix usage of default location from configuration
      [mpeeters]

    - Ensure that the marker is the main marker to fix geosearch
      [mpeeters]

- collective.faceted.map 1.0.0
    
    - Improve code to avoid to many refresh of the map
      [mpeeters]

- collective.geotransform 3.0

    - Add Plone 6 compatibility, drop Plone 5 support
      [boulch]

- imio.smartweb.core 1.1.4

    - Fix loader on React vue + add visual loader
      [thomlamb]

- imio.smartweb.common 1.1.2

    - Call @@consent-json view on navigation root (instead of context)
      [laulaz]

    - Ensure Ajax requests are always uncached
      [laulaz]

- imio.smartweb.core 1.1.3

    - WEB-3819 : Update permission : local manager can manage their subsites
      [boulch]

- imio.smartweb.core 1.1.2

    - Adding react-translated and translate static React txt
      [thomlamb]

    - Fix "zope.schema._bootstrapinterfaces.ConstraintNotSatisfied" in smartweb settings
      [boulch]

    - Add new content type : imio.smartweb.CirkwiView
      [boulch, laulaz]

    - Add authentic sources menu in toolbar
      [boulch, laulaz]

    - WEB-3755 : Adapt empty (without section) procedure message
      [boulch, laulaz]

    - Bring current-language attribute in rest views templates (useful for translations in JS)
      [boulch]

    - Handle search result types depending on available authentic sources for site
      [Julien]

    - Replacement of hard coded urls for images
      [thomlamb]

- imio.smartweb.policy 1.1.2

    - By default authorize_local_message and show_local_message in messagesviewlet must be True in smartweb
      [boulch]

- Update to Plone 6.0.0.2
  [laulaz]

- imio.smartweb.locales 1.1

    - Add DE translations (with copied French sentences for now)
      [laulaz]

    - Update buildout to Plone 6.0.0 final
      [laulaz]

- imio.smartweb.policy 1.1.1

    - Fix missing Plone icons (plone.staticresources)
      [laulaz]

    - Install and configure autopublishing (with 15 min tick subscriber)
      [laulaz]

    - Multilingual: add setup profile with content / default page migration to LRF
      and navigation links creation, fix selector viewlet
      [laulaz]

    - Remove obsolete TinyMCE override
      [laulaz]

- imio.smartweb.core 1.1.1

    - Use generated image scale urls to increase image caching
      [boulch, laulaz]

    - Forbid minisite to be copied / moved inside another minisite
      [laulaz]

    - Allow querying contact category with React filter (A) while also querying
      multiple categories defined in directory REST endpoint (B, C): A and (B or C)
      [laulaz]

    - Enable autopublishing behavior on all types
      [laulaz]

    - Handle events occurences in REST endpoint
      [laulaz]

    - Multilingual: handle language in requests for REST views, handle LRF navigation
      roots (minisites, footers, default pages, vocabularies), fix language selector
      viewlet
      [laulaz]

    - Add upgrade step to change content types icons
      [laulaz]

    - Fix JS / CSS bundles names (restore old names : '-' instead of '.' separator)
      [laulaz]

- imio.smartweb.common 1.1.1

    - Allow to choose language for vocabulary term translation
      [laulaz]

    - Use bootstrap dropdown-toggle for fieldsets collapse icon on edit forms
      [laulaz]

    - Fix TinyMCE menu bar and format menu
      [laulaz]

    - Update `widget.pt` override from `plone.app.z3cform.templates`
      [laulaz]

    - Improve monkeypatch to fix TTW resource calling
      [laulaz]

    - Update buildout to get Plone 6.0.0 final
      [laulaz]

- collective.messagesviewlet 1.0b2

    - Fix bundle registry upgrade step
      [laulaz]

- imio.smartweb.core 1.1

    - Update to Plone 6.0.0 final
      [boulch]

    - WEB-3795 : Add Proactive trigger code to chatbot.
      [remdub]

- imio.smartweb.common 1.1

    - Add monkeypatch to fix TTW resource calling See plone/Products.CMFPlone#3705
      [laulaz]

    - Uninstall collective.js.jqueryui
      [boulch]

    - Remove faceted deprecated bundles
      [boulch]

    - Migrate to Plone 6 : remove dexteritytextindexer, use new simplified
      resources registry, fix TinyMCE configuration and images scales,
      manual minimized js
      [laulaz, boulch]

- imio.smartweb.policy 1.1

    - Update to Plone 6.0.0 final
      [boulch]

    - WEB-3798 : Update caching profile (add lastModified to etags)
      [sverbois, remdub, boulch]

- collective.messagesviewlet 1.0b1

    - Migrate to Plone 6.0.0: remove dexteritytextindexer, use new simplified resources registry, fix styles, fix icons, ...
      [boulch, laulaz]

    - Add local messages feature. Local messages can be added in any folderish content types and you can choose if / on which levels they display.
      [boulch]

    - Protect messages-config folder with one-state private workflow.
      [boulch]

    - Add control panel (with messages-config folder link).
      [boulch]

    - Use JS to show/hide messages when closed, to avoid caching problems (#12).
      [laulaz]

    - Update / improve translations.
      [boulch, laulaz]

- Migrate to Plone 6.0.0 final and clean useless auto-checkout
  [boulch]


1.0.26 (2023-01-09)
-------------------

- Fix messagesviewlet source
  [boulch]


1.0.25 (2023-01-09)
-------------------

- imio.smartweb.locales 1.1

    - Add DE translations (with copied French sentences for now)
      [laulaz]

    - Update buildout to Plone 6.0.0 final
      [laulaz]


1.0.24-quick (2022-11-24)
-------------------------

- imio.smartweb.core 1.0.27

    - Add check for multiple categories directory views This is used to decide if the field will be changed to single category
      [laulaz]

- imio.smartweb.core 1.0.26

    - WEB-3729 : Add site admin permission on action for managing taxonomies on specific contents
      [boulch]

    - WEB-3777: Make nb_results field work on React views (as batch size)
      [laulaz, thomlamb]

- imio.smartweb.common 1.0.10

    - Ignore batch related query parameters for search-filters endpoint
      [laulaz]

- imio.smartweb.common 1.0.9

    - Add helper method to get language from smartweb REST requests
      This is needed for multilingual authentic sources
      [laulaz]

    - Allow to translate vocabulary terms titles in search-filters endpoint
      This is needed for multilingual authentic sources
      [laulaz]

- imio.smartweb.locales 1.0.8

    - Add missing French translations (Sendinblue, multilingual)
      [laulaz]


1.0.23 (2022-10-30)
-------------------

- imio.smartweb.locales 1.0.7

  - Add some directory fields translations
    [boulch]

  - Exclude profiles.zcml from translations
    [laulaz]

- imio.smartweb.core 1.0.25

  - WEB-3771 : Harmonize procedure button label
    [boulch]

  - WEB-3777 : Fix DirectoryEndpoint filter by category
    [boulch, laulaz]

  - WEB-3759 : Add portrait class even if there is no lead image to set placeholder with a good size
    [boulch]

- imio.smartweb.policy 1.0.10

  - Remove unneeded caching patches for 304 NOT MODIFIED requests Those are not needed anymore with the new cache configuration
    [laulaz]

- collective.sendinblue 2.0.3

  - Handle double opt-in
    [boulch, laz]

  - Fix typo in French
    [remdub]


1.0.22 (2022-10-21)
-------------------

- imio.smartweb.core 1.0.24

  - Fix problem with images url in logo
    [boulch]


1.0.21-quick (2022-10-20)
-------------------------

- imio.smartweb.core 1.0.23

  - Fix problem with images urls in collections
    [boulch]


1.0.20 (2022-10-18)
-------------------

- imio.smartweb.core 1.0.22

  - Fix problem with images urls in faceted navigation
    [laulaz]

  - WEB-3766 : Ensure displaying pages / footers even if sections in error (+ display section in error)
    [boulch, laulaz]

  - WEB-3764 : Fix : We Ensure we always compare Decimal
    [boulch]

- collective.anysurfer 1.4.7

  - Change permissions : By default, configlet should be accessible for Manager AND Site Administrator
    [boulch]

- collective.anysurfer 1.4.6

  - Fix import error for ILanguageSchema on Plone 5.2 / 6
    [laulaz]


1.0.19 (2022-10-17)
-------------------

- imio.smartweb.core 1.0.21
    - Waiting for authentics sources Plone6betaX to get automaticaly images scale hash on objects
      [boulch]

- imio.smartweb.policy 1.0.9

    - WEB-3733 : Restrict permissions for "site admin" in control panel. Some options are only available for manager
      [boulch]

    - Change s-maxage for new Varnish strategy based on grace
      [sverbois]

- imio.smartweb.core 1.0.20

    - Fix React-moment: replace 'day' by 'minute' in sratOf fuction to fix bad hours display in news view
      [thomlamb]

    - Add fullobjects=1 to get inner events and inner directory contents
      [boulch]

    - Adding section files download and gallery in react content view
      [thomlamb]

    - Update svg plone-icon for better compatibility with color css
      [thomlamb]

    - Use unique scale path (with hash) for better cache management
      [boulch, laz]

    - Memoize EventsTypesVocabulary because that almost never change !
      [boulch]

    - WEB-3684 : Add fullobjects=1 to get inner news contents
      [boulch]


1.0.18-quick (2022-09-08)
-------------------------

- imio.smartweb.core 1.0.19

    - WEB-3750 : Fix topics, categories and facilities items in selectboxes view when there is no preset selected categories
      [boulch]



1.0.17-quick (2022-09-06)
-------------------------

- imio.smartweb.core 1.0.18

    - Fix css to display none accueil item in nav
      [thomlamb]


1.0.16 (2022-09-04)
-------------------

- imio.smartweb.core 1.0.17

    - WEB-3741 : Fix items in selectbox contact categories in rest view @search-filters endpoint ("match" with items in edit selectbox)
      Fix contacts results depends of selected category in rest view (@search endpoint)
      [boulch]

    - WEB-3732 : Add smartweb settings to customize sendinblue subscribing button (text and position)
      [boulch]

    - Fix bad position for swipper-button in herobanner
      [thomlamb]

    - Ensure navigation elements don't use an already reserved/existing css Class
      [boulch]

    - WEB-3730 : By default, Plone open external (Section text / Tiny) links in new tab
      [boulch]

- imio.smartweb.policy 1.0.8

    - WEB-3731 : Automatically publish GDPR article
      [boulch]

- imio.smartweb.common 1.0.8

    - MWEB-54 : Update TinyMCE : Add non breaking space option
      [boulch]


1.0.15 (2022-08-02)
-------------------

- imio.smartweb.core 1.0.16

    - Fix rich description display on contact section
      [laulaz]

- imio.smartweb.core 1.0.15

    - WEB-3687: Add botpress viewlet in footer
      [remdub]

    - Change class and css to make herobanner slider work
      [thomlamb]


1.0.14-quick (2022-07-18)
-------------------------

- pas.plugins.imio 2.0.6

    - Do not verify_signature for jwt call because of error: "Could not deserialize key data".
      [bsuttor]


1.0.13 (2022-07-14)
-------------------

- imio.smartweb.core 1.0.14

    - Avoid error on broken objects (reindex_all_pages upgrade step)
      [laulaz]


1.0.12-quick (2022-07-14)
-------------------------

- imio.smartweb.core 1.0.13

    - Adding button for add news,events,contacts
      [thomlamb]

    - Avoid traceback if a selection item relation is broken
      [laulaz]

    - Use rich description on contact sections
      [laulaz]

    - [WEB-3674]Fix itinerary links
      [remdub]

    - [WEB-3661]Set b_size to 100 on search results
      [remdub]

    - Add collective.faceted.map with custom template & markers popups
      [boulch, laulaz]

    - Allow pages to be geolocalized (latitude/longitude indexes) via their first map section
      [laulaz]

    - Use new registry settings to store URL of news/events/contact proposal form
      [laulaz]

- imio.smartweb.locales 1.0.6

    - Add Dutch translations files
      [laulaz]

    - Add faceted map translation
      [laulaz]

    - Add propose URLs translations
      [laulaz]


1.0.11 (2022-07-13)
-------------------

- pas.plugins.imio 2.0.5

    - Keep old roles on migration of users.
      [bsuttor]

    - Temporary remove pas.app.users override because it do not work on Plone 6.
      [bsuttor]

    - Add possibility to remove old user (without login).
      [bsuttor]


1.0.10 (2022-07-13)
-------------------

- Upgrade collective.taxonomy to 2.2.2 (to allow edition for site administrators)
  [laulaz]

- pas.plugins.imio 2.0.3

    - Migration code refactoring & add tests
      [laulaz]

    - Add migration code (to new userid) for local roles / ownership
      [laulaz]


1.0.9 (2022-06-13)
------------------

- imio.smartweb.locales 1.0.5

    - Add translation for Agent connection
      [laulaz]

- imio.smartweb.common 1.0.7

    - Add connection link in colophon
      [laulaz]

- imio.smartweb.core 1.0.12

    - [WEB-3663] Fix contact schedule. Use Decimal instead of float. ( float("8.30") = 8.3. 8h03 != 8h30 )
      [boulch]

    - Update static css for edit view
      [thomlamb]

    - Fix NaN value for batchsize in swiper
      [thomlamb]

    - Ban required URL when Footer or HeroBanner modified
      [boulch, laulaz]

    - Omit some fields in slide section layout fieldset
      [boulch]

- imio.smartweb.policy 1.0.7

    - Adapt SolR config to use tika for file indexing
      [mpeeters]

    - Move/adapt ban_physicalpath method into imio.smartweb.common
      [boulch, laulaz]

- imio.smartweb.common 1.0.6

    - Add ban_physicalpath method (taken from policy)
      [boulch, laulaz]

- pas.plugins.imio 2.0

    - Get userid and user login for user connected by JWT.
      [bsuttor]

    - Allow user search on any parts of id/login/email (not just the start)
      [laulaz]

    - Use uuid as plone user.id instead of username.
      [bsuttor, laulaz]

    - Be aware of next url when you call auhentic users api.
      [bsuttor]

    - Add zmi view of users.
      [bsuttor]


1.0.8 (2022-05-30)
------------------

- Upgrade collective.taxonomy to 2.2.1
  [laulaz]

- Update buildout and setuptools.
  [bsuttor]

- Change p.a.imagecropping source to stay at the same rev (waiting for Plone next release)
  [laulaz]


1.0.7 (2022-05-17)
------------------

- imio.smartweb.core 1.0.11

    - Update display for date in news view
      [thomlamb]

    - Add video,social,web url for news view
      [thomlamb]

    - Update regex for routing items
      [thomlamb]

    - Add carousel and gallery in contact view
      [boulch]

    - Fix batch size (40) for pages pagination
      [laulaz]

    - Add new content type : imio.smartweb.SectionPostit
      [boulch, laulaz]

- imio.smartweb.locales 1.0.4

    - Add translations for contact gallery
      [laulaz]

    - Add translations for post-it section
      [laulaz]


1.0.6 (2022-05-16)
------------------

- imio.smartweb.common 1.0.5

    - Refactor rich description to retrieve html on a any description (from context or from other ways)
      [boulch]

- imio.smartweb.common 1.0.4

    - Limit uploaded files sizes to 20Mo with JS (without reaching the server)
      [laulaz]

    - Add help text on lead image field also on edit forms
      [laulaz]

- imio.smartweb.core 1.0.10

    - Add description for directory items
      [thomlamb]

    - Fix css for react items
      [thomlamb]

    - Adaptation of the jsx to be able to render the markdown to html
      [thomlamb]

    - Adapt `@search` endpoint to exclude expired elements and events in the past
      [mpeeters]

    - Remove forced placeholder for image in react pages
      [thomlamb]


1.0.5-quick (2022-05-02)
------------------------

- imio.smartweb.core 1.0.9

    - Remove duplicate / useless new icons & change default workinfos icon
      [laulaz]

- imio.smartweb.core 1.0.8

    - Add new icons
      [boulch]

    - Fix section edition display for herobanner / content-core / footer
      [laulaz]

    - HeroBanner can't be a folder default view
      [boulch]

- imio.smartweb.common 1.0.3

    - Hide faceted actions
      [boulch]

- imio.smartweb.policy 1.0.6

    - Remove collective.z3cform.select2. We don't use full product anymore
      [boulch]

- imio.smartweb.locales 1.0.3

    - Add translation for image upload
      [laulaz]

    - Add translations for new icons
      [laulaz]

- imio.smartweb.locales 1.0.2

    - Add Hero banner related translations
      [laulaz]


1.0.4-quick (2022-04-25)
------------------------

- imio.smartweb.policy 1.0.5

    - Uninstall collective.z3cform.select2, not needed anymore for faceted
      [laulaz]

    - Hide unwanted upgrades from site-creation and quickinstaller
      [boulch]

    - Add missing viewlet + reorder viewlets
      [boulch]

- imio.smartweb.common 1.0.2

    - Hide unwanted upgrades from site-creation and quickinstaller
      [boulch]

    - Add local manager role and sharing permissions rolemap
      [boulch]

    - Add help text on lead image fields
      [boulch]

    - Fix privacy views JS calls (sometimes called on Zope root instead of Plone root)
      [laulaz]

    - Add Subject keywords to SearchableText index
      [laulaz]


1.0.3-quick (2022-04-25)
------------------------

- imio.smartweb.core 1.0.7

    - Improve slide view html
      [thomlamb]

    - Clean core css
      [thomlamb]

    - Fix herobanner when there is a default (portal)page on site root or on partner sites
      [boulch]

    - Hide unwanted upgrades from site-creation and quickinstaller
      [boulch]

    - Move local manager role and sharing permissions to imio.smartweb.common
      Use new common.interfaces.ILocalManagerAware to mark a locally manageable content
      [boulch]

    - Add hero banner feature
      [boulch]

- Use released version for collective.z3cform.select2
  [laulaz]


1.0.2-quick (2022-03-29)
------------------------

- imio.smartweb.core 1.0.6

    - Fix: Change Leaflet Tilelayer map for fix bad attribution url
      [thomlamb]

- Remove gunicorn timeout to allow long requests
  [laulaz]

- imio.smartweb.policy 1.0.4

    - Add etags userid and roles in caching configuration
      [sverbois, boulch]

    - Adapt ban_for_message to cover multi varnish servers and add http to correctly ban
      [boulch]

    - Allow some Python modules in RestrictedPython (code moved from smartweb.core)
      This is useful for collective.themefragments fragments
      [boulch]

- imio.smartweb.core 1.0.5

    - Add local permissions and a "Local Manager" role.
      Permissions : imio.smartweb.core.CanEditMinisiteLogo, imio.smartweb.core.CanManageSectionHTML
      [boulch]

    - Updated queries for search to only run with specific filters
      [thomlamb]

    - Handle inline SVG images for portal logo and minisite logo
      [laulaz]

    - Add show_items_lead_image attributes on files section.
      Add no-image css class in table template when there is no image to display
      [boulch]

    - Add sections to procedure content type to be similar as page content type
      [boulch]

    - Add a portrait mode on section contact leadimage
      [boulch]

    - Exclude parents (folders) messages to traverse into partners sites
      [boulch]

    - Exclude Footers from parent listings by default
      [laulaz]

- imio.smartweb.locales 1.0.1

    - Add missing translation for Local Manager & lead image portrait mode
      [laulaz]

- imio.smartweb.core 1.0.4

    - Improve leaflet css
      [thomlamb]

    - Change leaflet tilelayer style
      [thomlamb]

- imio.smartweb.policy 1.0.3

    - add logger to get some informations about BAN with Varnish
      [boulch]

    - Fix collective autoscaling default values
      [boulch]

- Switch collective.solr from auto-checkout to 9.0.0a6 pinned version
  [boulch]

- imio.gdpr 1.2.2

    - Remove plone.app.registry template override as it is now released:
      Plone 6.0.0a3 / plone.app.registry 2.0.0a7
      [laulaz]

    - Add specific controlpanel permission and give this permission to site administrator
      [boulch]


1.0.1-quick (2022-03-16)
------------------------

- imio.smartweb.common 1.0.1

    - Allow readers, editors and reviewers to see inactive (expired) contents
      [laulaz]

- Update collective.solr checkout revision to include inactive content fix
  [laulaz]

- Use https:// instead of git:// protocol
  See https://github.blog/2021-09-01-improving-git-protocol-security-github/
  [laulaz]

- imio.smartweb.core 1.0.3

    - Change leaflet style
      [thomlamb]

    - Adding info popup on leaflet marker
      [thomlamb]

    - Add correct href on search link for tab navigation
      [thomlamb]

- imio.smartweb.locales 1.0

    - Change 'minisite' to 'site partenaire' in French
      [laulaz]

    - Add icon field related translations
      [laulaz]

- imio.smartweb.common 1.0

    - Avoid traceback if @@get_analytics is called outside Plone site
      [laulaz]

- imio.smartweb.core 1.0.2

    - Add missing init file for faceted widgets
      [laulaz]

- imio.smartweb.policy 1.0.2

    - Add/install select2 widget for faceted
      [boulch]

    - Fix BAN request when we change a message
      [boulch, laulaz]

- Add pytest to verify policy is installed.
  [bsuttor]

- imio.smartweb.policy 1.0.1

    - Add missing zcml include of collective.autoscaling
      [laulaz]

    - Fix faceted criteria update when installing from code (without browser request)
      [laulaz]

- Use collective.recipe.template 2.2 to avoid use_2to3 errors on Github
  [laulaz]

- imio.smartweb.core 1.0.1

    - Removal of the pointer if it is located at Imio (event and library view)
      [thomlamb]

    - Added times and fixed date display for event views
      [thomlamb]

    - Override eea.facetednavigation select widget template.
      Display label as first value in select fields
      [boulch]

    - Add placeholder to faceted text search (xml) + upgrade step
      [boulch]

    - Fix : Add a missing tal instruction
      [boulch]

    - Use new icons radio widget to select SVG icon for links
      [laulaz]

    - Avoid problems with minisite & subsite simultaneous activation (for example,
      through a cached action)
      [laulaz]

- Improve docker HEALTHCHECK.
  [bsuttor]


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
