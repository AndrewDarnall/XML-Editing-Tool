""" The file contains string and type definitions used in the xml_editor.py file """

from typing import Tuple, Dict

# Replacements dict type alias
ReplacementsDict = Dict[str, Tuple[str, Tuple[str, str]]]

ADD_STRING_1 = (
    "<ReferenceCoded>\n"
    "    <ReferenceTypeCoded>Other</ReferenceTypeCoded>\n"
    "    <ReferenceTypeCodedOther>Version</ReferenceTypeCodedOther>\n"
    "    <PrimaryReference>\n"
    "        <Reference>\n"
    "            <RefNum>1</RefNum>\n"
    "        </Reference>\n"
    "    </PrimaryReference>\n"
    "</ReferenceCoded>"
)

ADD_STRING_2 = (
    "<ReferenceCoded>\n"
    "    <ReferenceTypeCoded>Other</ReferenceTypeCoded>\n"
    "    <ReferenceTypeCodedOther>Percent</ReferenceTypeCodedOther>\n"
    "    <PrimaryReference>\n"
    "        <Reference>\n"
    "            <RefNum>100</RefNum>\n"
    "        </Reference>\n"
    "    </PrimaryReference>\n"
    "</ReferenceCoded>"
)

EDIT_STRING = (
    "<Party>\n"
    "    <PartyID>\n"
    "        <Identifier>\n"
    "            <Agency>\n"
    "                <AgencyCoded>Other</AgencyCoded>\n"
    "                <AgencyCodedOther>GruppoTelecomItalia</AgencyCodedOther>\n"
    "            </Agency>\n"
    "            <Ident>A890</Ident>\n"
    "        </Identifier>\n"
    "    </PartyID>\n"
    "    <NameAddress>\n"
    "        <Name1>FiberCop S.p.A.</Name1>\n"
    "        <Street>VIA GAETANO NEGRI 1</Street>\n"
    "        <PostalCode>20123</PostalCode>\n"
    "        <City>MILANO</City>\n"
    "        <Region>\n"
    "            <RegionCoded>MI</RegionCoded>\n"
    "        </Region>\n"
    "        <Country>\n"
    "            <CountryCoded>IT</CountryCoded>\n"
    "        </Country>\n"
    "    </NameAddress>\n"
    "</Party>"
)
