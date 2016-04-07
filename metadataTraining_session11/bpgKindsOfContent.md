Best Practice Guidelines for describing different kinds of subject matter
==================================================================

##Table of Contents

1. Describing Subject Matter
2. Assigning Subject Terms
  - Which Subject Terms Go Where
  - Forming Subject Terms

## 1. Describing Subject Matter

Regardless of medium (image, text, sound, etc.) subject matter is always present. For example, you might have one image that is about a memorial service for the SEVEN, an Iowa State University women's cross-country team who died in a plane crash. You might have another image that is about Morrill Hall, a building on the Iowa State University campus. These different subject matter can be boiled down to different types of subject matter. The first example is a type of event. The second is a type of building.

These different types have implications in how you describe the images. When describing a type of event, you might describe the people and their interactions in detail, whereas when describing a type of building, you might highlight important features of the building and its environment. There might be multiple types of subject matter present within one image. For example, you might have an image of an Iowa State University men's basketball game (event) that is being held in Hilton Coliseum (building). In this case, you need to determine which type of subject matter is most important. This will drive how you describe the image.

## 2. Assigning Subject Terms

### Which Subject Terms Go Where

There are five possible metadata fields where you can assign subject terms: "Subject", "Geographic Subject", "Organizations", "People", and "Events". Use the most appropriate field first. For instance, if you want to assign a place name, assign it to "Geographic Subject" rather than "Subject". For our purposes, building names will fall under "Geographic Subject" as a location. Specific personal names fall under "People", corporate names fall under "Organizations", etc. Types of people fall under "Subject" (e.g. "College students"). Assign types of events or occurrences to "Events". For example, "Memorial service" and "Cross-country running". If you want to assign a term that does not fit under "Geographic Subject", "Organizations", "People", or "Events", assign it to "Subject". It is okay to assign a general term, such as "Memorial service", and a more specific term, such as "Memorial service for the SEVEN", to the same field. This will give us the ability to facet for resources about all memorial services, as well as resources specifically about the memorial service for the SEVEN.

### Forming Subject Terms

First, search Library of Congress authorities for an appropriate term. If there isn't one, search our local authorities within Aleph. If there isn't an authorized term in either, create a new term. When creating a new term, adhere to Library of Congress best practices for that type of term. For example, corporate names follow the following format: "Iowa State University. Department of Athletics", while building names follow the following format: "Morrill Hall (Ames, Iowa)".

When creating a new corporate name or building name, use the full form of its name as it was at the time of the resource you are describing (ex. "ISU Chamber Singers", even though that's not its current name). If you know that the corporate body or building was/is known under a different name, you can add that name as an additional subject term. This is optional, and you shouldn't invest time researching this unless suggested otherwise.

When creating a new personal name, use the preferred form of the name, that is, how they are commonly referred to as (ex. "H. G. Wells" instead of "Herbert George Wells"). If you do not know how they are referred, use the fullest form of their name.

### Assigning Broader Subject Terms

One functionality that we want in ContentDM is filtering. Use-cases of faceting can include the following:

- *User wants to find all photographs of "Morrill Hall (Ames, Iowa)"*
- *User wants to find all photographs of all places on "Iowa State University" campus*

Humans can infer that "Morrill Hall (Ames, Iowa)" is a place on the "Iowa State University" campus, but this is not apparent to a machine like ContentDM. So, the only way to meet both use-cases is to assign both "Morrill Hall (Ames, Iowa)" and "Iowa State University". This holds true for corporate names as well. Given:

- *User wants to find all photographs associated with "Iowa State University. Department of Athletics. Wrestling"*
- *User wants to find all photographs associated with "Iowa State University. Department of Athletics"*
- *User wants to find all photographs associated with "Iowa State University"*

One would have to assign "Iowa State University. Department of Athletics. Wrestling", "Iowa State University. Department of Athletics", and "Iowa State University".

When assigning corporate and place names that fall under "Iowa State University", assign the term and all broader terms up to "Iowa State University", as seen in both previous use-case examples.
